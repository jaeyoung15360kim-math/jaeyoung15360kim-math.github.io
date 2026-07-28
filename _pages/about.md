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

I am a Ph.D. student in the [Department of Mathematical Sciences](https://math.snu.ac.kr) at **Seoul National University (SNU)**, working under the supervision of [Prof. Seonhee Lim](https://www.math.snu.ac.kr/~lim/research.html) in the [DASOM](https://www.math.snu.ac.kr/~lim/DASOM.html) research group.

<p class="contact-links">
  <a href="mailto:jaeyoungkim22@snu.ac.kr"><i class="fa-solid fa-envelope" aria-hidden="true"></i> jaeyoungkim22@snu.ac.kr</a>
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
