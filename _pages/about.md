---
layout: about
title: Jaeyoung Kim
permalink: /
subtitle: PhD Student, Department of Mathematical Sciences, Seoul National University
nav: false
social: false

announcements:
  enabled: false
latest_posts:
  enabled: false
---

<style>
  .name-container {
    text-align: center;
    margin: 1em 0 1.5em 0;
  }
  
  .name-container h1 {
    font-size: 2.2em;
    margin: 0;
    line-height: 1.4;
    letter-spacing: 0.02em;
  }
  
  .name-s, .name-m, .name-k {
    cursor: pointer;
    transition: color 0.2s ease;
  }
  
  .name-s:hover, .name-m:hover, .name-k:hover {
    font-weight: 600;
  }
  
  .english-name {
    white-space: nowrap;
  }
</style>

<div class="name-container">
  <h1>
    <span class="english-name">
      <span class="name-s"
            onmouseover="document.querySelectorAll('.name-s').forEach(x => x.style.color='#D99700')"
            onmouseout="document.querySelectorAll('.name-s').forEach(x => x.style.color='inherit')">Jae</span><span class="name-m"
            onmouseover="document.querySelectorAll('.name-m').forEach(x => x.style.color='#0077B6')"
            onmouseout="document.querySelectorAll('.name-m').forEach(x => x.style.color='inherit')">young</span>
      <span class="name-k"
            onmouseover="document.querySelectorAll('.name-k').forEach(x => x.style.color='#D1495B')"
            onmouseout="document.querySelectorAll('.name-k').forEach(x => x.style.color='inherit')">Kim</span>
    </span>
    <br>
    (<span class="name-k"
          onmouseover="document.querySelectorAll('.name-k').forEach(x => x.style.color='#D1495B')"
          onmouseout="document.querySelectorAll('.name-k').forEach(x => x.style.color='inherit')">김</span><span class="name-s"
          onmouseover="document.querySelectorAll('.name-s').forEach(x => x.style.color='#D99700')"
          onmouseout="document.querySelectorAll('.name-s').forEach(x => x.style.color='inherit')">재</span><span class="name-m"
          onmouseover="document.querySelectorAll('.name-m').forEach(x => x.style.color='#0077B6')"
          onmouseout="document.querySelectorAll('.name-m').forEach(x => x.style.color='inherit')">영</span>
    /
    <span class="name-k"
          onmouseover="document.querySelectorAll('.name-k').forEach(x => x.style.color='#D1495B')"
          onmouseout="document.querySelectorAll('.name-k').forEach(x => x.style.color='inherit')">金</span><span class="name-s"
          onmouseover="document.querySelectorAll('.name-s').forEach(x => x.style.color='#D99700')"
          onmouseout="document.querySelectorAll('.name-s').forEach(x => x.style.color='inherit')">才</span><span class="name-m"
          onmouseover="document.querySelectorAll('.name-m').forEach(x => x.style.color='#0077B6')"
          onmouseout="document.querySelectorAll('.name-m').forEach(x => x.style.color='inherit')">永</span>)
  </h1>
</div>

I am a Ph.D. student in the [Department of Mathematical Sciences](https://math.snu.ac.kr) at **Seoul National University (SNU)**, working under the supervision of [Prof. Seonhee Lim](https://www.m[...])

<p class="contact-links">
  <span class="contact-email"><i class="fa-solid fa-envelope" aria-hidden="true"></i> <span id="contact-email" class="email-protected"></span></span>
  <noscript>Email available with JavaScript enabled.</noscript>
  <span aria-hidden="true">·</span>
  <a href="{{ '/assets/pdf/CV_Jaeyoung_Kim.pdf' | relative_url }}"><i class="fa-solid fa-file-pdf" aria-hidden="true"></i> Curriculum Vitae</a>
</p>

### Research Interests

My primary research area is **Homogeneous Dynamics** of higher-rank Lie groups over real or non-Archimedean local fields, together with Ergodic Theory and dynamics on buildings.

---

### Education & Academic Career

<ul class="education-list">
  {% for entry in site.data.site_cv.education %}
    <li>
      <strong>{{ entry.title }}</strong> | {{ entry.institution }} ({{ entry.date }})
      {% if entry.details %}<br><span>{{ entry.details }}</span>{% endif %}
    </li>
  {% endfor %}
</ul>
