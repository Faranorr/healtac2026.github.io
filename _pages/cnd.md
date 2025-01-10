---
permalink: /datesandcalls/
title: "Calls and Dates"
---

<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: sans-serif;
}
.collapsible {
  background-color:#003865;
  color:  white;
  cursor: pointer;
  padding: 30px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-family: sans-serif;
  font-size: 30px;
}
.active, .collapsible:hover {
  background-color: #0999;
  color: black;
}
.collapsible:after {
  content: '\002B';
  color: white;
  font-weight: bold;
  float: right;
  margin-left: 10px;
  font-family: sans-serif;
}
.active:after {
  content: "\2212";
}
.content {
  padding: 2px 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
}
mark { 
  background-color:  rgba(150, 212, 212, 0.4);
  color: black;
}
/* Float three columns side by side */
.column {
  float: left;
  width: 30%;
  padding: 0 5px;
}
/* Remove extra left and right margins, due to padding */
.row {margin: 0 -5px;}
/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
/* Style the counter cards table*/
.card-1 {
  box-shadow: 0 2px 6px 0 rgba(0.2, 0.2, 0.2, 0.2);
  padding: 10px;
  text-align: center;
  background-color: white;
  color:black;
}
.card {
  padding: 10px;
  text-align: center;
  background-color: #000999;
  color: black; 
  text-shadow: 0.1px 0.1px;
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
  margin-bottom: 6px;
  padding: 0 6px;
}
.container {
  padding: 0 52px;
}
.container::after, .row::after {
  content: "";
  clear: both;
  display: table;
}
th, td {
  text-align: left;
  padding: 10px;
}
td {
  border-bottom: 1px solid #ddd;
}
div.gallery img {
  width: 50%;
  height: auto;
}
div.desc {
  padding: 5px;
  text-align: center;
}
* {
  box-sizing: border-box;
}
.clearfix:after {
  content: "";
  display: table;
  clear: both;
}
</style>
</head>
<body>
<br>
<button class="collapsible">Call for contributions</button>
<div class="content">
<p>Healthcare narrative (such as clinical notes, discharge letters, nurse handover notes, imaging reports, patients posts on social media or feedback comments, etc.) has been used as a key communication stream that contains the majority of actionable and contextualised healthcare data, but which – despite being increasingly available in a digital form – is not routinely analysed, and is rarely integrated with other healthcare data on a large-scale. There are many barriers and challenges in processing healthcare free text, including, for example, the variability and implicit nature of language expressions, and difficulties in sharing training and evaluation data. On the other hand, recent years have witnessed increasing opportunities to process free text, with a number of success stories that have demonstrated the feasibility of using advanced Natural Language Processing to unlock evidence contained in free text to support clinical care, patient self-management, epidemiological research and audit.</p>

<h2 style="color:#009999;">Topics</h2>
<p> HealTAC 2025 invites contributions that address any aspect of healthcare text analytics, including (but not limited to) the following topics: </p>
<p> </p>
<ul>
      <li>(Large) language models for healthcare text analytics</li>
  
       <li>Machine-learning approaches to healthcare text analytics</li>

       <li>Transfer learning for healthcare text analytics</li>
 
       <li>Speech analytics for healthcare applications</li>

       <li>Processing clinical literature and trial reports</li>
       
       <li>Multi-modal models for healthcare decision support</li>
  
       <li>Text analytics and learning health systems</li>
   
       <li>Healthcare ontologies and coding of healthcare text</li>
   
       <li>Explainable models for healthcare NLP</li>
   
       <li>Real-time processing of healthcare free text</li>
 
       <li>Real-world application of healthcare text analytics</li>
  
       <li>Scalable and secure healthcare NLP infrastructures</li>

       <li>Text mining for veterinary medicine</li>

       <li>Privacy-preserving healthcare analytics</li>
 
       <li>Datasets for healthcare text analytics</li>

       <li>Reproducibility in the healthcare text analytics</li>
  
       <li>Evaluation and assessment of text analytics methods</li>
 
       <li>Sharing resources for healthcare text analytics (data and methods)</li>

       <li>Information extraction: identification of clinical variables and their values in free-text</li>
   
       <li>Processing patient-generated data (e.g. social media, health forums, diaries)</li>
   
       <li>Implementation of healthcare text analytics in practice: public engagement and governance</li>
 </ul>
 <br>
</div>

<!-- <button class="collapsible">Second call for contributions</button>
<div class="content">
<p>The 8th Healthcare Text Analytics Conference (HealTAC 2025) invites contributions that address any aspect of healthcare text analytics. This year, we invite submissions in the form of extended abstracts that describe either methodological or application work that has not been previously presented in a conference. Submissions (up to 2 pages) should be prepared based on a template that is available at the conference website. 
We also invite PhD and fellowship project submissions that describe ongoing PhD research (any stage) or a planned fellowship application. The conference will provide an opportunity to receive constructive feedback from a panel of experts.
As in previous years, there will be a post-conference open call to submit a journal-length paper for further peer review and publication in Frontiers in Digital Health.</p>  -->

<!-- <h3>Submission site:</h3> -->
<!-- <p><mark>https://easychair.org/conferences/?conf=healtac2025</mark></p> -->
<!-- <p>TBD</p> -->

<!-- <h3>Updated key dates :</h3>
    <p><mark>Deadline for all contributions: <b>April 8th 2025</b></mark></p>
    <p><mark>Notification of acceptance: <b>April 24th 2025</b></mark></p>
    <p><mark>Tutorial: <b>June 12th 2025</b></mark></p>
    <p><mark>Conference: <b>June 13-14th 2025</b></mark></p>

<h3> Keynote speakers </h3>
<p>We are pleased to announce that the keynote speakers at HealTAC 2025 will be:
<b>Suzan Verberne</b> (Leiden University) and <b>Alistair Johnson</b> (Glowyr). </p>

<h3> Tutorial </h3>
<p>We are also pleased that a team from the Institute of Health Informatics, University College London (Yunsoo Kim, Jinge Wu, Honghan Wu) will deliver a tutorial on <b>'Healthcare Text Analytics in the Era of Large Language Models'</b>.</p>

<h3>Announcements </h3>
<p>Follow the conference announcements on social media at <mark><b>#HEALTAC2025</b></mark></p>
<p>We are looking forward to welcoming you to HealTAC 2025.</p>
</div> -->

<button class="collapsible">Submissions</button>
<div class="content">
<h2>Contribution types</h2>
<h4 style="color:#009999;">Extended abstracts</h4>
TBC
<!-- Extended abstracts will describe either methodological or application work that has not been previously presented in a conference. Contributions should be prepared based on a template. Authors will specify their preferred way of presenting their contribution: as an oral presentation, flash/lightning talk, poster or demo. As in previous years, there will be a post-conference open call to submit a journal-length paper for further peer review and publication in Frontiers in Digital Health.  We have already published four issues following the previous HealTAC events. <b>Contributions should consist of up to 2 pages, excluding references</b>. -->

<h4 style="color:#009999;">PhD and fellowship projects</h4>
TBC
<!-- Submissions by PhD students or early career researchers will be presented at the separate forum. These should present ongoing PhD research (in any stage) or a planned fellowship application. The forum will provide an opportunity to receive constructive feedback from the community, including a panel that will consist of the keynote speakers and experts in different areas. Contributions should consist of up to 4 pages and will be treated separately from the other submissions. -->

<h4 style="color:#009999;">Panel discussions</h4>
TBC
<!-- Panel discussions can be proposed to address the main challenges in processing healthcare free-text or to discuss the future of particular methodologies. Panels will be allocated one hour slots for discussions. Proposals for panels should consist of up to 2 pages. -->

<h4 style="color:#009999;">Software demo sessions</h4>
TBC
<!-- Demo sessions will provide a forum for demonstration of solutions and projects to the wider community. Proposals for demos should use the template for extended abstracts. -->
                                                                                                                                          
<h4 style="color:#009999;">Submission Template</h4>
TBC
<!-- The submission template can be accessed here: <a href="https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fhealtac2025%2Fhealtac2025.github.io%2Fmain%2F_data%2Ftemplate-2025.docx&wdOrigin=BROWSELINK" download>Word</a>, <a href="https://github.com/healtac2025/healtac2025.github.io/raw/main/_data/Template-HealTAC2022.zip" download>Latex</a>, <a href="https://www.overleaf.com/latex/templates/healtac2025-template/sqgwgbcqsmdx " download>Overleaf</a>  -->
<!-- <br>
<p>Please use <a href="https://easychair.org/conferences/?conf=healtac2025">Easychair</a> for all submissions.</p><br> -->
</div>

<button class="collapsible">Important Dates</button>
<div class="content">
 <div class="column">
    <div class="card-1">
    <br>
      <div class="container">
        <p>All deadlines are 11:59PM UTC-12:00 (“anywhere on Earth”).</p>
        <p>TBC</p>
<!-- <table>
  <tr>
    <th>Event</th>
    <th>Date</th>
  </tr>
  
  <tr>
    <td>First Call</td>
    <td>February 2nd, 2025</td>
  </tr>
  
  <tr>
    <td>Submission template available</td>
    <td>February 2nd, 2025</td>
  </tr> 
  
  <tr>
    <td>Latex template available</td>
    <td>March 21st, 2025</td>
  </tr>
  
  <tr>
    <td>Submission site available</td>
    <td>March 22nd, 2025</td>
  </tr>
  
  <tr>
    <td>Deadline for all contributions</td>
    <td><del>March 28th, 2025</del> April 8th 2025</td>
  </tr>

  <tr>
  	<td>Notification of acceptance</td>
    <td><del>April 19th, 2025</del> April 24th, 2025</td>
  </tr>
  
  <tr>
    <td>Tutorial</td>
    <td>June 12th, 2025 </td>
  </tr>
  
  <tr>
    <td>Conference</td>
    <td><del>June 12-14th 2025</del> June 13-14th 2025</td>
  </tr>
</table> -->
      </div>
    <br>
    </div>
  </div>
</div>

<!-- <button class="collapsible">Sponsors</button>
<div class="content">
<br>
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://www.frontiersin.org/">
      <img src="https://idd.nationalcoreindicators.org/wp-content/uploads/2022/08/frontiers-logo-with-bg.png" width="100%" height="100%">
    </a>
    <p>Frontiers Media S.A.</p>
  </div>
</div>
<br>
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="https://www.lancaster.ac.uk/dsi/">
      <img src="https://cisweb.lancaster.ac.uk/EventsMedia/dsi-637837307099205167.png">
    </a>
    <p>Data Science Institute, Lancaster University, UK</p>
  </div>
</div>
<br>
<div class="responsive">
  <div class="gallery">
    <a target="_blank" href="http://healtex.org/">
      <img src="https://stroke.wales/wp-content/uploads/2018/11/healtex.gif">
    </a>
    <p>UK Healthcare Text Analytics Network</p>
  </div>
</div>
</div> -->

<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
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
</script>

</body>
</html>
