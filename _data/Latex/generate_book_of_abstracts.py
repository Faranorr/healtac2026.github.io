#!/usr/bin/env /opt/homebrew/bin/python3.11
"""
Generate HealTAC 2026 Book of Abstracts PDF.

Reads the submissions CSV and individual abstract PDFs, produces a single PDF
with a cover page, clickable table of contents (sorted A–Z by first author's
last name), and the abstracts appended in that order.

Excludes paper #12 (author requested no publication).

Usage:
    cd <repo-root>
    ./_data/Latex/generate_book_of_abstracts.py
    # Output: _data/Book_of_Abstracts.pdf
"""

import csv
import unicodedata
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.annotations import Link
from pypdf.generic import RectangleObject
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO        = Path(__file__).resolve().parents[2]
SUBMISSIONS = Path('/Users/leopold/Downloads/submissions')
CSV_PATH    = Path('/Users/leopold/Downloads/abstracts-details(Submissions).csv')
OUTPUT_PDF  = REPO / '_data' / 'Book_of_Abstracts.pdf'
ASSETS      = REPO / 'assets' / 'images'
SPONSORS    = ASSETS / 'sponsors'
BANNER      = ASSETS / 'banner-brighton.jpg.jpeg'

SPONSOR_LOGO_FILES = [
    SPONSORS / 'dareuk.png',
    SPONSORS / 'HDR UK.jpg',
    SPONSORS / 'kcl-logo.svg',       # SVG — handled via cairosvg
    SPONSORS / 'BSMS-Logo-Black.jpg',
    ASSETS   / 'safetext.png',        # lives in main assets/, not sponsors/
    SPONSORS / 'CogStack.png',
    SPONSORS / 'Frontiers.jpg',
    SPONSORS / 'maudsley_logo.png',
]

EXCLUDED_PAPERS = {'12', '10'}  # authors asked not to publish

# Manual corrections for CSV data errors
AUTHOR_CORRECTIONS = {
    '19': 'Samuel Thio, David Tang, James Teo, Thomas Searle and Richard Dobson',
}

# Words to skip when building initials (titles/conjunctions)
_SKIP_WORDS = {'and', 'dr', 'dr.', 'prof', 'prof.', 'mr', 'mr.', 'ms', 'ms.', 'mrs', 'mrs.'}

# ── Colours (r, g, b floats 0–1) ─────────────────────────────────────────────
TEAL      = (0,       0.600, 0.600)
BLUE      = (0.392,   0.584, 0.929)
DARK_GREY = (0.3,     0.3,   0.3)
MID_GREY  = (0.55,    0.55,  0.55)
LIGHT_BG  = (0.95,    0.97,  1.0)
WHITE     = (1, 1, 1)
BLACK     = (0, 0, 0)

# Type badge colours (background, text)
BADGE_COLOURS = {
    'Long Talk':     ((0.0,  0.55, 0.55), WHITE),
    'Lightning':     ((0.25, 0.55, 0.85), WHITE),
    'Poster':        ((0.45, 0.45, 0.75), WHITE),
    'Demo':          ((0.65, 0.40, 0.80), WHITE),
    'PhD Talk':      ((0.20, 0.65, 0.45), WHITE),
    'PhD Lightning': ((0.20, 0.65, 0.45), WHITE),
    'Accepted':      ((0.5,  0.5,  0.5),  WHITE),
}

W, H = A4  # 595.27 × 841.89 pt

MARGIN_X   = 2.0 * cm
MARGIN_TOP = 2.2 * cm
MARGIN_BOT = 2.0 * cm

# ── Utilities ─────────────────────────────────────────────────────────────────

_SORT_REPLACEMENTS = str.maketrans({
    'æ': 'ae', 'Æ': 'ae',
    'ø': 'o',  'Ø': 'o',
    'å': 'a',  'Å': 'a',
    'œ': 'oe', 'Œ': 'oe',
    'ß': 'ss',
})

def strip_diacritics(s: str) -> str:
    s = s.translate(_SORT_REPLACEMENTS)
    return ''.join(c for c in unicodedata.normalize('NFKD', s)
                   if not unicodedata.combining(c))


def _get_first_author(authors: str) -> str:
    """Extract the first author's full name, handling both comma and 'and' separators."""
    first_chunk = authors.split(',')[0].strip()
    # If no comma separated authors, split on ' and '
    if ' and ' in first_chunk.lower():
        first_chunk = first_chunk.split(' and ')[0].strip()
    # Strip leading title words (Dr, Prof, etc.)
    words = [w for w in first_chunk.split() if w.lower() not in _SKIP_WORDS]
    return ' '.join(words)


def entry_sort_key(authors: str, title: str = '') -> tuple:
    """Sort by (last name, initials, title) — all case-folded, diacritics stripped."""
    first = _get_first_author(authors)
    words = first.split()
    last = words[-1] if words else first
    initials = ''.join(w[0] for w in words[:-1] if w and w.lower() not in _SKIP_WORDS)
    return (
        strip_diacritics(last).casefold(),
        strip_diacritics(initials).casefold(),
        strip_diacritics(title).casefold(),
    )


def first_author_display(authors: str) -> str:
    """Format first author as 'Lastname, F.I.' [et al.]"""
    has_more = (',' in authors) or (' and ' in authors.lower())
    first_full = _get_first_author(authors)
    words = first_full.split()
    if not words:
        return authors
    last = words[-1]
    initials = ''.join(
        w[0] + '.' for w in words[:-1]
        if w and w.lower() not in _SKIP_WORDS
    )
    display = f"{last}, {initials}" if initials else last
    if has_more:
        display += ' et al.'
    return display


def decision_label(decision: str) -> str:
    d = decision.lower()
    if 'oral' in d:                return 'Long Talk'
    if 'lightning' in d:           return 'Lightning'
    if 'demo' in d:                return 'Demo'
    if 'phd' in d and 'talk' in d: return 'PhD Talk'
    if 'phd' in d:                 return 'PhD Lightning'
    if 'poster' in d:              return 'Poster'
    return 'Accepted'


def _svg_to_pil(path: Path) -> PILImage.Image | None:
    """Convert an SVG file to a PIL Image via cairosvg."""
    try:
        import cairosvg
        png_bytes = cairosvg.svg2png(url=str(path), scale=4)  # scale=4 for sharp rendering
        return PILImage.open(BytesIO(png_bytes))
    except Exception as e:
        print(f'  ⚠  Cannot convert SVG {path.name}: {e}')
        return None


def pil_to_reader(path: Path, max_px: int = 1600, jpeg_quality: int = 85) -> ImageReader | None:
    """
    Load an image file into a reportlab ImageReader.

    max_px    – longest edge is capped at this many pixels (keeps file size down).
    jpeg_quality – quality used when saving photos as JPEG (logos with transparency
                   are still saved as PNG to preserve their alpha channel).
    """
    try:
        if path.suffix.lower() == '.svg':
            img = _svg_to_pil(path)
            if img is None:
                return None
        else:
            img = PILImage.open(str(path))

        # Downsample very large images before embedding
        if max(img.size) > max_px:
            img.thumbnail((max_px, max_px), PILImage.LANCZOS)

        buf = BytesIO()
        # Use JPEG for opaque photos — much smaller than PNG for photographic content
        if img.mode == 'RGBA' or 'transparency' in getattr(img, 'info', {}):
            img.save(buf, format='PNG', optimize=True)
        else:
            img = img.convert('RGB')
            img.save(buf, format='JPEG', quality=jpeg_quality, optimize=True)
        buf.seek(0)
        return ImageReader(buf)
    except Exception as e:
        print(f'  ⚠  Cannot load {path.name}: {e}')
        return None


def image_display_size(path: Path, target_h: float, max_w: float):
    """Return (w, h) display size scaled to target_h, capped at max_w."""
    try:
        if path.suffix.lower() == '.svg':
            img = _svg_to_pil(path)
        else:
            img = PILImage.open(str(path))
        if img is None:
            return max_w, target_h
        orig_w, orig_h = img.size
        scale = target_h / orig_h
        w = min(orig_w * scale, max_w)
        h = target_h * (w / (orig_w * scale)) if (orig_w * scale) > max_w else target_h
        return w, h
    except Exception:
        return max_w, target_h


def is_blank_page(page) -> bool:
    """Return True if the page has no visible content (no text, no images)."""
    if '/Contents' not in page:
        return True
    try:
        if (page.extract_text() or '').strip():
            return False
    except Exception:
        pass
    # Pages with only images have no extractable text — check for XObject resources
    try:
        resources = page.get('/Resources', {})
        if '/XObject' in resources:
            return False
    except Exception:
        pass
    return True


def is_poster_page(page) -> bool:
    """Return True if the page is much larger than A4 (i.e. a conference poster)."""
    mb = page.mediabox
    area = float(mb.width) * float(mb.height)
    return area > 3 * W * H


def prescan_entries(entries: list[dict]) -> list[dict]:
    """
    Pre-scan each abstract PDF to determine which pages to include
    (skipping blank and poster pages) and assign book page start numbers.
    Mutates entries in place, adding 'include_pages' and 'book_start'.
    """
    book_page = 1
    for entry in entries:
        try:
            r = PdfReader(str(entry['pdf']))
            include = []
            for i, page in enumerate(r.pages):
                if is_blank_page(page):
                    print(f"    Paper {entry['num']}: skipping blank page {i + 1}")
                elif is_poster_page(page):
                    mb = page.mediabox
                    print(f"    Paper {entry['num']}: skipping poster page {i + 1} "
                          f"({float(mb.width):.0f}x{float(mb.height):.0f} pt)")
                else:
                    include.append(i)
            entry['include_pages'] = include
            entry['book_start'] = book_page
            book_page += len(include)
        except Exception as e:
            print(f"  ⚠  Cannot scan paper {entry['num']}: {e}")
            entry['include_pages'] = []
            entry['book_start'] = book_page
    return entries


def truncate_text(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars - 1].rstrip() + '…'


# ── CSV parsing ───────────────────────────────────────────────────────────────

def parse_csv() -> list[dict]:
    entries = []
    with open(CSV_PATH, encoding='cp1252') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if len(row) < 4:
                continue
            num      = row[0].strip()
            authors  = row[1].strip().replace('\n', ' ')
            title    = row[2].strip().replace('\n', ' ')
            decision = row[3].strip()

            if num in EXCLUDED_PAPERS:
                print(f'  Skipping paper {num} (excluded)')
                continue
            if not any(x in decision.lower() for x in ('accept', 'phd')):
                continue

            # Apply manual corrections
            if num in AUTHOR_CORRECTIONS:
                authors = AUTHOR_CORRECTIONS[num]

            pdf = SUBMISSIONS / f'HealTAC_2026_paper_{num}.pdf'
            if not pdf.exists():
                print(f'  ⚠  PDF missing: paper {num}')
                continue

            entries.append({
                'num':     num,
                'authors': authors,
                        'title':   title,
                        'label':   decision_label(decision),
                        'pdf':     pdf,
                        'sort_key': entry_sort_key(authors, title),
                        'display':  first_author_display(authors),
                    })

    entries.sort(key=lambda e: e['sort_key'])
    print(f'  {len(entries)} entries loaded and sorted')
    return entries


# ── Front-matter PDF generation ───────────────────────────────────────────────

def draw_cover(c: rl_canvas.Canvas):
    """Draw the cover page onto the current canvas page."""
    # Banner
    banner_h = 210
    banner_reader = pil_to_reader(BANNER)
    if banner_reader:
        c.drawImage(banner_reader, 0, H - banner_h, width=W, height=banner_h,
                    preserveAspectRatio=False, mask='auto')
    else:
        c.setFillColorRGB(*TEAL)
        c.rect(0, H - banner_h, W, banner_h, fill=1, stroke=0)

    # Conference names
    y = H - banner_h - 38
    c.setFont('Helvetica-Bold', 30)
    c.setFillColorRGB(*TEAL)
    c.drawCentredString(W / 2, y, 'HealTAC 2026')

    y -= 26
    c.setFont('Helvetica', 15)
    c.setFillColorRGB(*DARK_GREY)
    c.drawCentredString(W / 2, y, 'Health Text Analytics Conference')

    y -= 50
    c.setFont('Helvetica-Bold', 38)
    c.setFillColorRGB(*BLUE)
    c.drawCentredString(W / 2, y, 'Book of Abstracts')

    y -= 30
    c.setFont('Helvetica', 13)
    c.setFillColorRGB(*DARK_GREY)
    c.drawCentredString(W / 2, y, '8–10 June 2026  ·  Brighton, UK')

    y -= 18
    c.setFont('Helvetica', 10)
    c.setFillColorRGB(*TEAL)
    c.drawCentredString(W / 2, y, 'healtac2026.github.io')

    # Rule
    y -= 22
    c.setStrokeColorRGB(*TEAL)
    c.setLineWidth(1.2)
    c.line(MARGIN_X, y, W - MARGIN_X, y)

    # Sponsors heading
    y -= 18
    c.setFont('Helvetica-Bold', 9)
    c.setFillColorRGB(*MID_GREY)
    c.drawCentredString(W / 2, y, 'SPONSORS & PARTNERS')

    # Sponsor logos
    TARGET_H = 36
    MAX_W    = 90
    GAP      = 10
    usable_w = W - 2 * MARGIN_X

    logo_sizes = []
    for path in SPONSOR_LOGO_FILES:
        if path.exists():
            lw, lh = image_display_size(path, TARGET_H, MAX_W)
            ir = pil_to_reader(path)
            if ir:
                logo_sizes.append((ir, lw, lh))

    # Pack into rows
    rows: list[list] = []
    row: list = []
    row_w = 0.0
    for ir, lw, lh in logo_sizes:
        needed = lw + (GAP if row else 0)
        if row and row_w + needed > usable_w:
            rows.append(row)
            row = [(ir, lw, lh)]
            row_w = lw
        else:
            row.append((ir, lw, lh))
            row_w += needed
    if row:
        rows.append(row)

    y -= 12
    for row in rows:
        total_w = sum(lw for _, lw, _ in row) + GAP * (len(row) - 1)
        x = MARGIN_X + (usable_w - total_w) / 2
        row_h = max(lh for _, _, lh in row)
        for ir, lw, lh in row:
            c.drawImage(ir, x, y - lh, width=lw, height=lh,
                        preserveAspectRatio=True, mask='auto')
            x += lw + GAP
        y -= row_h + GAP

    c.showPage()


def draw_toc(c: rl_canvas.Canvas, entries: list[dict]) -> list[dict]:
    """
    Draw the table of contents.  Returns a list of link descriptors:
        {'toc_page': int, 'rect': (x1, y1, x2, y2)}
    one per entry, in the same order as `entries`.
    The toc_page is 0-based within the front-matter PDF (cover = page 0).
    """
    links = []
    toc_page = 1  # cover is page 0

    BADGE_W    = 68
    BADGE_H    = 11
    LINE_H     = 18
    ENTRY_PAD  = 4       # extra gap between entries
    PAGE_NUM_W = 28      # space reserved on right for the page number
    CONTENT_X  = MARGIN_X + BADGE_W + 8
    USABLE_W   = W - MARGIN_X - CONTENT_X - PAGE_NUM_W - 4

    def start_toc_page():
        nonlocal toc_page
        y = H - MARGIN_TOP
        # Heading
        c.setFont('Helvetica-Bold', 18)
        c.setFillColorRGB(*BLUE)
        c.drawString(MARGIN_X, y, 'Contents')
        y -= 10
        c.setStrokeColorRGB(*BLUE)
        c.setLineWidth(1)
        c.line(MARGIN_X, y, W - MARGIN_X, y)
        y -= 16
        return y

    y = start_toc_page()

    for entry in entries:
        label   = entry['label']
        display = entry['display']
        title   = entry['title']  # full title, no truncation

        # Estimate height: author on one line, title may wrap
        title_chars_per_line = int(USABLE_W / 5.2)  # ~5.2 pt per char at 8.5pt
        title_lines = max(1, -(-len(title) // title_chars_per_line))  # ceil div
        entry_h = max(BADGE_H + 6, (title_lines + 1) * LINE_H * 0.75) + ENTRY_PAD + 6

        if y - entry_h < MARGIN_BOT:
            c.showPage()
            toc_page += 1
            y = start_toc_page()

        row_top    = y
        row_bottom = y - entry_h + ENTRY_PAD

        # Badge — anchored to row_top so it sits beside the author name
        badge_y = row_top - 13  # centres the badge on the author text baseline
        bg, fg = BADGE_COLOURS.get(label, BADGE_COLOURS['Accepted'])
        c.setFillColorRGB(*bg)
        c.roundRect(MARGIN_X, badge_y, BADGE_W, BADGE_H, 2, fill=1, stroke=0)
        c.setFont('Helvetica-Bold', 7)
        c.setFillColorRGB(*fg)
        c.drawCentredString(MARGIN_X + BADGE_W / 2, badge_y + 2.5, label.upper())

        # Author
        c.setFont('Helvetica-Bold', 8.5)
        c.setFillColorRGB(*DARK_GREY)
        author_text = truncate_text(display, 30)
        c.drawString(CONTENT_X, row_top - 10, author_text)

        # Page number (right-aligned, same baseline as author)
        c.setFont('Helvetica', 8.5)
        c.setFillColorRGB(*MID_GREY)
        c.drawRightString(W - MARGIN_X, row_top - 10, str(entry['book_start']))

        # Title
        c.setFont('Helvetica', 8.5)
        c.setFillColorRGB(*BLACK)
        # Simple wrapping
        words = title.split()
        line_buf = ''
        ty = row_top - 22
        for word in words:
            test = (line_buf + ' ' + word).strip()
            if c.stringWidth(test, 'Helvetica', 8.5) > USABLE_W:
                c.drawString(CONTENT_X, ty, line_buf)
                ty -= LINE_H * 0.75
                line_buf = word
            else:
                line_buf = test
        if line_buf:
            c.drawString(CONTENT_X, ty, line_buf)

        # Thin separator
        sep_y = row_bottom + ENTRY_PAD
        c.setStrokeColorRGB(*LIGHT_BG)
        c.setLineWidth(0.4)
        c.line(MARGIN_X, sep_y, W - MARGIN_X, sep_y)

        # Record clickable area (full row)
        links.append({
            'toc_page':   toc_page,
            'rect':       (MARGIN_X, sep_y, W - MARGIN_X, row_top),
            'book_start': entry['book_start'],
        })

        y = sep_y - 2

    c.showPage()
    return links


def generate_front_matter(entries: list[dict]) -> tuple[bytes, list[dict]]:
    """Render cover + ToC to an in-memory PDF. Return (pdf_bytes, link_descriptors)."""
    buf = BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=A4)
    draw_cover(c)
    links = draw_toc(c, entries)
    c.save()
    buf.seek(0)
    return buf.read(), links


# ── Page number overlay ───────────────────────────────────────────────────────

def make_page_number_overlay(book_page: int, page_w: float, page_h: float) -> bytes:
    """
    Generate a single-page PDF containing only a book-level page number.
    The number is placed at the very bottom centre (y=8 pt) in small grey
    italic, styled as  — N —  to distinguish it from the submission's own
    pagination.
    """
    buf = BytesIO()
    c = rl_canvas.Canvas(buf, pagesize=(page_w, page_h))
    c.setFont('Helvetica-Oblique', 7.5)
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.drawCentredString(page_w / 2, 8, f'— {book_page} —')
    c.showPage()
    c.save()
    buf.seek(0)
    return buf.read()


# ── Merge and annotate ────────────────────────────────────────────────────────

def build_pdf(entries: list[dict], front_bytes: bytes, links: list[dict]):
    writer = PdfWriter()

    # 1. Add front-matter pages (no page numbers on cover/ToC)
    front_reader = PdfReader(BytesIO(front_bytes))
    n_front = len(front_reader.pages)
    for page in front_reader.pages:
        writer.add_page(page)

    # 2. Add abstract PDFs, overlay sequential book page numbers
    page_offset = n_front
    book_page = 1  # abstract pages numbered from 1

    for entry in entries:
        try:
            r = PdfReader(str(entry['pdf']))
            for i in entry['include_pages']:
                page = r.pages[i]
                mb = page.mediabox
                pw = float(mb.width)
                ph = float(mb.height)
                # Normalize to A4 if the page is a different size
                if abs(pw - W) > 2 or abs(ph - H) > 2:
                    sx, sy = W / pw, H / ph
                    page.add_transformation(Transformation().scale(sx=sx, sy=sy))
                    page.mediabox.upper_right = (W, H)
                    pw, ph = W, H
                # Overlay the book page number
                overlay_bytes = make_page_number_overlay(book_page, pw, ph)
                overlay_page = PdfReader(BytesIO(overlay_bytes)).pages[0]
                page.merge_page(overlay_page)
                writer.add_page(page)
                book_page += 1
            page_offset += len(entry['include_pages'])
        except Exception as e:
            print(f"  ⚠  Skipping paper {entry['num']}: {e}")

    # 3. Add link annotations to ToC entries
    for link_desc in links:
        target_idx = n_front + link_desc['book_start'] - 1
        page_num = link_desc['toc_page']
        x1, y1, x2, y2 = link_desc['rect']
        annotation = Link(
            rect=RectangleObject([x1, y1, x2, y2]),
            target_page_index=target_idx,
        )
        writer.add_annotation(page_number=page_num, annotation=annotation)

    # 4. Lossless stream compression (zlib-deflate any uncompressed content streams)
    for page in writer.pages:
        page.compress_content_streams()

    # 5. Write output
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PDF, 'wb') as f:
        writer.write(f)

    size_before = OUTPUT_PDF.stat().st_size
    print(f'\n  ✓ Written: {OUTPUT_PDF}')
    print(f'    Front matter:   {n_front} pages (no numbers)')
    print(f'    Abstract pages: {book_page - 1} pages (numbered 1–{book_page - 1})')
    print(f'    Total:          {page_offset} pages')
    print(f'    File size:      {size_before / 1e6:.1f} MB')

    # 6. Ghostscript post-pass: downsample images in submitted PDFs to 150 DPI
    _compress_with_ghostscript(OUTPUT_PDF)


def _compress_with_ghostscript(pdf_path: Path, quality: str = 'printer'):
    """
    Re-encode the merged PDF with Ghostscript to shrink embedded images.

    'ebook' targets 150 DPI — good for on-screen reading and occasional printing.
    Falls back silently if gs is not installed.
    """
    import shutil, subprocess
    gs = shutil.which('gs')
    if not gs:
        print('  ℹ  Ghostscript not found — skipping lossy image compression.')
        print('     Install with: brew install ghostscript')
        return

    tmp = pdf_path.with_suffix('.gs_tmp.pdf')
    try:
        result = subprocess.run(
            [
                gs, '-dBATCH', '-dNOPAUSE', '-dQUIET',
                '-sDEVICE=pdfwrite',
                '-dCompatibilityLevel=1.5',
                # Keep all images at their original resolution — no downsampling
                '-dDownsampleColorImages=false',
                '-dDownsampleGrayImages=false',
                '-dDownsampleMonoImages=false',
                # Still recompress images (lossless where possible)
                '-dAutoFilterColorImages=false',
                '-dColorImageFilter=/FlateEncode',
                '-dAutoFilterGrayImages=false',
                '-dGrayImageFilter=/FlateEncode',
                f'-sOutputFile={tmp}',
                str(pdf_path),
            ],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode == 0 and tmp.exists():
            orig = pdf_path.stat().st_size
            new  = tmp.stat().st_size
            tmp.replace(pdf_path)
            print(f'  Ghostscript (lossless): '
                  f'{orig / 1e6:.1f} MB → {new / 1e6:.1f} MB  '
                  f'({100 * (1 - new / orig):.0f}% smaller)')
        else:
            print(f'  ⚠  Ghostscript failed (rc={result.returncode}): '
                  f'{result.stderr[:300]}')
            if tmp.exists():
                tmp.unlink()
    except subprocess.TimeoutExpired:
        print('  ⚠  Ghostscript timed out after 5 min')
        if tmp.exists():
            tmp.unlink()
    except Exception as e:
        print(f'  ⚠  Ghostscript error: {e}')
        if tmp.exists():
            tmp.unlink()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print('HealTAC 2026 — Book of Abstracts generator\n')
    print('Parsing CSV...')
    entries = parse_csv()

    print('Pre-scanning PDFs (blank/poster detection, page numbering)...')
    entries = prescan_entries(entries)

    print('Generating front matter (cover + ToC)...')
    front_bytes, links = generate_front_matter(entries)

    print(f'Merging {len(entries)} PDFs...')
    build_pdf(entries, front_bytes, links)


if __name__ == '__main__':
    main()
