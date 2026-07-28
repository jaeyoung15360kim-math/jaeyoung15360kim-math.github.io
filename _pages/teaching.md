---
layout: page
permalink: /teaching/
title: Teaching
description: Teaching assistantships, grading experiences, and instructional activities at Seoul National University.
nav: true
nav_order: 6
---

<ul class="teaching-list">
  {% for entry in site.data.site_cv.teaching %}
    <li><strong>{{ entry.title }}</strong> | {{ entry.institution }} ({{ entry.date }})</li>
  {% endfor %}
</ul>
