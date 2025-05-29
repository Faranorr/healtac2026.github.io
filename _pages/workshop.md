---
permalink: /workshop/
title: "Pre-conference Workshop: Mental health and the New NLP"
---
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
<style>
body {
  font-family: sans-serif;
}
html {
  box-sizing: border-box;
}
*, *:before, *:after {
  box-sizing: inherit;
}
.column {
  float: left;
  width: auto;
  margin-bottom: 16px;
  padding: 0 0px;
  font-family: Times New Roman;
}
@media screen and (max-width: 650px) {
  .column {
    width: auto;
    display: block;
  }
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}
.container {
  padding: 0 0px;
}
.container::after {
  content: "";
  clear: both;
  display: table;
}
.title {
  color: grey;
}
.button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
}
.button:hover {
  background-color: #009999;
}
.collapsible {
  background-color:  #F0F8FF;
  color: #6495ED;
  cursor: pointer;
  padding: 8px;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}
.active, .collapsible:hover {
  background-color: #6495ED;
  color: black;
}
.content {
  padding: 0 8px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  font-size: 14px;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
  var coll = document.getElementsByClassName("collapsible");
  for (var i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.maxHeight){
        content.style.maxHeight = null;
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  }
});
</script>
<p>Workshop is open to all. If you are interested in presenting at the workshop, please email <span>angus.roberts at kcl.ac.uk</span> with a short abstract for consideration.</p>

<p>This one day workshop is organised by <a href="https://datamind.org.uk/">DATAMIND - The Health Data Research Hub for Mental Health</a>, the hub for mental health informatics research development. Whilst <a href="https://datamind.org.uk/">DATAMIND</a> has a specific focus on mental health, it is expected that the workshop will be of interest and relevance to people from across the entire health text analytics community. The workshop will consider application of the "New NLP" to all aspects of mental health: research, clinical care and therapy.</p>

<p>The advent of large language models and generative AI is bringing about a sea change in natural language processing, has provided new perspectives on many of the challenges that have faced health-related NLP, and is opening up new research directions. We can now extend the reach of NLP, with the processing of complex language that assumes domain expertise and pragmatic understanding becoming more tractable. We have new solutions to perennial problems: where once we talked about the challenges of obtaining access to restricted health record text, we can now realistically discuss generating high-quality synthetic records, and where we struggled to find domain expert time for data labelling, we now consider using generative AI annotators. Beyond research, many are considering ways in which generative AI can play a role in therapeutic settings. The new NLP also raises many concerns, including those of bias; the ethics and ownership of models built from patient data; and the availability, financial and environmental cost of the processing power required to train ever-larger models.</p>

<p>This one day workshop will bring together attendees from informatics, clinical, industry and service user backgrounds to discuss the shift in NLP and what it means for mental health. The morning will focus on technical challenges and innovations, with the afternoon given to papers and discussions of broader operational, clinical, and societal implications.</p>

<h5 style="margin-bottom: 0.9375rem; font-weight: bold; line-height: 1.1; color: #6495ED; font-size: 0.9375rem; clear: both; text-transform: uppercase; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; text-align: start; padding-top: 20px;">Abstracts</h5>
<button class="collapsible">Dr Marcos Del Pozo Banos, Senior Lecturer in Health Data Science, Swansea University <br>
‘The journey of AI and NLP in mental health research’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">Artificial intelligence (AI) and natural language processing (NLP) have evolved from early rule-based programs (e.g., the 1966 ELIZA chatbot) to data-driven statistical and neural models. Recent innovations in deep learning – including word embeddings, recurrent neural networks, and Transformer-based architectures – have unlocked new capabilities for mining and interpreting large text corpora, transforming the landscape of mental health research. Key applications include: extracting structured information from electronic health records; performing sentiment and semantic analysis of social media posts for early detection; and deploying therapeutic chatbots to deliver scalable psychological support. Looking forward, researchers are integrating large pre-trained language models with multimodal inputs to personalise diagnostics and interventions. However, there are still many technical and ethical challenges to address, including model interpretability, clinical integration, data privacy, algorithmic bias, and transparency.</p></div>

<button class="collapsible">
Arlene Casey, Vivensa Foundation Senior Research Fellow, University of Edinburgh<br>
‘Insight and Exposure: NLP for Mental Health and the Challenge of Protecting Privacy’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
Mental health narratives in clinical free-text contain crucial insights - such as references to suicide, depression, or trauma - that researchers need but which also pose privacy risks. We will talk about our ongoing work with NLP and large language models (LLMs) to detect these sensitive disclosures, not only to protect patient identity, but also how this is being used to support research and service improvement in the NHS.
  </p></div>

<button class="collapsible">
Dr Jaya Chaturvedi, Research Associate in Health-Related NLP, King’s College London
  <br>
‘Implicature in Mental Health Medical Records’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
Clinical notes in mental health records contain rich textual data capturing information about the patient. This work analyzes the extent to which implicature is used to describe important clinical concepts, and whether the extraction of such implied concepts is possible with large language models.
</p></div>

<button class="collapsible">
Darren Cook, Research Fellow in NLP, City St George's / VISION consortium
  <br>
TBC
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
</p></div>

<button class="collapsible">
Dr Maximilian Droog-Hayes, Principal AI Scientist, ieso Health
  <br>
‘Responsible Innovation in Mental Healthcare: Developing Digital Interventions Safely with Generative AI’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
Since it was established in the year 2000, ieso has treated over 145,000 patients and collected data from over 815,000 hours of therapy sessions to build the world's largest outcomes-indexed mental health dataset. This talk will summarize our research into increasing access to mental healthcare through responsible innovation and the safe use of cutting-edge AI models and techniques.
</p></div>


<button class="collapsible">
Matthew Iveson, Senior Research Fellow, and Matúš Falis, Research Fellow & Associate NLP Analyst, University of Edinburgh	
  <br>
‘Measuring Antidepressant Response: Reclassification of Undercoded Primary Care Encounters According to Relevance to Depression with Large Language Models’	
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
While people living with depression do not respond to antidepressants or take time to find a treatment that works for them, our understanding of who will respond and why has been limited by methodological challenges. In the AMBER project, we use both structured and unstructured electronic health record data to produce new measures of antidepressant response and non-response, enabling personalised medicine and risk prediction. In this talk we will present our work with primary care text data labelled by GPs with structured Read codes as part of routine practice. We will focus on filling in the gaps in the patients' depression timelines through identifying undercoded generic consultation encounters relevant to the depression phenotype with the aid of LLMs.
</p></div>



<button class="collapsible">
Dr Jorge Palacios, Chief Science Officer, Bright Therapeutics
  <br>
TBC
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
</p></div>

<button class="collapsible">
Dr Rashmi Patel, Assistant Professor in Real-World Data Analytics, University of Cambridge
  <br>
‘Beyond diagnostic classification: Characterising clinical phenotype and outcomes using NLP’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
In this talk I will describe how natural language processing can be applied to real-world datasets comprising insurance claims and electronic health record (EHR) data to provide novel insights into the clinical outcomes of people with mental disorders.
</p></div>


<button class="collapsible">
Gloria Roque, AI Product Owner, and Jack Richmond, AI Scientist, Akrivia Health
  <br>
  ‘Efficient and Reliable Validation of Clinical NLP models: Tackling Annotation Burden and Unbiased Recall Estimation’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
A significant portion of psychiatric electronic health records (EHRs) exists as unstructured free-text notes, posing challenges for large-scale data analysis and clinical decision-making. Natural Language Processing (NLP) offers a way to extract structured information from this text, but ensuring these models perform reliably, particularly in terms of recall, remains a major challenge. We present a validation methodology for Named Entity Recognition (NER) models that addresses both the annotation burden and the difficulty of accurately estimating recall by using stratified sampling with screening methods. This approach enables scalable, reliable evaluation of NLP models, aligning with the clinical demands of safe, accountable AI in healthcare.
</p></div>


<button class="collapsible">
Dr Jane Taylor, Patient Advocate, DATAMIND Super-Research Advisory Group
  <br>
  ‘Six degrees of separation’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
This talk will look at some of the issues in using NLP in electronic health records from the perspective of patients/ service users. It will focus on the filters used by both patient and health professionals before, during and after clinical encounters. It will consider what can be missed out or misinterpreted in these transcriptions – the importance of context and the significance of what cannot be said or heard. It will also look briefly at the bias which can arise in clinical encounters in terms of perceptions of status, gender, ethnicity and sexuality and how this can affect the terminology used to describe the patient’s feelings and symptoms.
</p></div>

<button class="collapsible">
Jytoi Sanyal, NLP Lead – Operational, SLaM NHSFT
  <br>
‘The evolution of NLP in the CRIS dataset’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
NLP has changed a lot over last couple of years. In my talk, I want to discuss how NLP methods have evolved over last 10 years in CRIS. What are the challenges we faced, not only in terms of methods but also operational challenges. How we manged to solve them and run these methods over large datasets.
</p></div>

<button class="collapsible">
Prof Rob Stewart, Professor of Psychiatric Epidemiology and Clinical Informatics, King’s College London
  <br>
‘Beyond coding – NLP strategy and application’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
Mental healthcare text presents sizeable challenges for NLP, although also huge opportunities to transform research capability. Given the time and resources required for code and algorithm developments, it is important that these are strategically focused and then effectively applied and utilised. This requires the assembly of a collaborative ecosystem between NLP developers and a range of stakeholders – another challenge, but also a rewarding opportunity.
</p></div>


<button class="collapsible">
Dr Jingyuan Sun, Lecturer in NLP and Text Mining, University of Manchester
  <br>
‘The Convergent Frontier: How GenAI, Neuroscience, and Mental Health Research are Uniting’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
This talk will first highlight the current dynamic interactions between Generative AI and neuroscience, GenAI and mental health applications, and the established synergy between neuroscience and mental health research. We will then explore the profound potential when these three domains fully unite. This powerful convergence promises to transform our understanding of mental illness, paving the way for more personalised diagnostics, novel therapeutic interventions, and a deeper comprehension of mental well-being.
</p></div>



<button class="collapsible">
Dr Tao Wang, Research Fellow in Heath Text Analytics and Data Science, King’s College London
  <br>
‘Building Medical Timeline for Clinical Text Using Large Language Models’
</button>
<div class="content">
  <p style=" color: black; background-color: white; text-decoration: none;">
Understanding clinical timelines from clinical narratives is critical for accurate diagnosis and effective treatment. Traditional methods for temporal reasoning often depend on rule-based approaches or simple models that struggle to capture the complexity and nuance of clinical language. While large language models (LLMs) hold promise, their capabilities in temporal reasoning remain underexplored. In this work, we construct a new benchmark dataset based on the i2b2 corpus to evaluate LLM performance in clinical temporal information extraction and reasoning. Preliminary results highlight both the potential and current limitations of LLMs in this domain.
</p></div>
