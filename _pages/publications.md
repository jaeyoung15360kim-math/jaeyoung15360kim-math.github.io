---
layout: page
permalink: /publications/
title: Publications
description: Publications and current research listed in my CV.
nav: true
nav_order: 2
---

<ol class="publication-list">
  {% for publication in site.data.site_cv.publications %}
    {% assign details = site.data.publication_details[publication.id] %}
    <li class="publication-entry">
      <h2 class="publication-title">{{ publication.title }}</h2>
      <p class="publication-authors">{{ publication.authors }}</p>
      <p class="publication-venue">
        {% if details.journal_url %}
          <a href="{{ details.journal_url }}">{{ publication.venue }}</a>
        {% else %}
          {{ publication.venue }}
        {% endif %}
        {% if publication.year %} ({{ publication.year }}){% endif %}
      </p>
      {% if details.arxiv_url %}
        <p class="publication-links"><a href="{{ details.arxiv_url }}">arXiv</a></p>
      {% endif %}
      {% if details.abstract %}
        <details class="publication-abstract">
          <summary>Abstract</summary>
          <p>{{ details.abstract }}</p>
        </details>
      {% endif %}
    </li>
  {% endfor %}
</ol>
