---
layout: about
title: About
permalink: /
subtitle: ""
nav: false
social: false

announcements:
  enabled: false
latest_posts:
  enabled: false
---

<style>
  /* Hide the duplicate title on the homepage; keep the header brand visible. */
  .post-title {
    display: none !important;
   }

  .name-container {
    text-align: left;
    margin: 0 0 1.5em 0;
  }

  .name-container h1 {
    font-size: 2.8em;
    margin: 0.5em 0 0.5em 0;
    line-height: 1.2;
    letter-spacing: 0.02em;
    font-weight: 700;
  }

  .name-s, .name-m, .name-k {
    cursor: pointer;
    transition: color 0.2s ease;
  }

  .name-s:hover, .name-m:hover, .name-k:hover {
    font-weight: 700;
  }
  
.profile-photo {
  float: right;
  width: min(32%, 13rem);
  margin: 0 0 1rem 2rem;
}
.profile-photo img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 8px;
}
.profile-photo-trigger {
  display: block;
  width: 100%;
  padding: 0;
  border: 0;
  background: transparent;
  cursor: zoom-in;
}

.profile-photo-dialog {
  max-width: 92vw;
  max-height: 92vh;
  padding: 1rem;
  border: 0;
  border-radius: 0.75rem;
  background: var(--bg-primary);
  overflow: auto;
}

.profile-photo-dialog::backdrop {
  background: rgb(0 0 0 / 80%);
}

.profile-photo-dialog img {
  display: block;
  width: auto;
  max-width: 88vw;
  max-height: 84vh;
  object-fit: contain;
  cursor: zoom-in;
}

.profile-photo-dialog-controls {
  display: flex;
  justify-content: flex-end;
  margin: 0 0 0.5rem;
}

.profile-photo-close {
  padding: 0.35rem 0.7rem;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  background: var(--bg-secondary);
  color: var(--text-primary);
  cursor: pointer;
}

.contact-links {
  clear: both;
}

@media (max-width: 600px) {
  .profile-photo {
    width: min(38%, 10rem);
    margin-left: 1rem;
  }
}  
</style>

<div class="name-container">
  <h1>
    <span class="name-s"
          onmouseover="document.querySelectorAll('.name-s').forEach(x => x.style.color='#D99700')"
          onmouseout="document.querySelectorAll('.name-s').forEach(x => x.style.color='inherit')">Jae</span><span class="name-m"
          onmouseover="document.querySelectorAll('.name-m').forEach(x => x.style.color='#0077B6')"
          onmouseout="document.querySelectorAll('.name-m').forEach(x => x.style.color='inherit')">young</span>
    <span class="name-k"
          onmouseover="document.querySelectorAll('.name-k').forEach(x => x.style.color='#D1495B')"
          onmouseout="document.querySelectorAll('.name-k').forEach(x => x.style.color='inherit')">Kim</span>
    (<span class="name-k"
          onmouseover="document.querySelectorAll('.name-k').forEach(x => x.style.color='#D1495B')"
          onmouseout="document.querySelectorAll('.name-k').forEach(x => x.style.color='inherit')">김</span><span class="name-s"
          onmouseover="document.querySelectorAll('.name-s').forEach(x => x.style.color='#D99700')"
          onmouseout="document.querySelectorAll('.name-s').forEach(x => x.style.color='inherit')">재</span><span class="name-m"
          onmouseover="document.querySelectorAll('.name-m').forEach(x => x.style.color='#0077B6')"
          onmouseout="document.querySelectorAll('.name-m').forEach(x => x.style.color='inherit')">영</span>
    / <span class="name-k"
          onmouseover="document.querySelectorAll('.name-k').forEach(x => x.style.color='#D1495B')"
          onmouseout="document.querySelectorAll('.name-k').forEach(x => x.style.color='inherit')">金</span><span class="name-s"
          onmouseover="document.querySelectorAll('.name-s').forEach(x => x.style.color='#D99700')"
          onmouseout="document.querySelectorAll('.name-s').forEach(x => x.style.color='inherit')">才</span><span class="name-m"
          onmouseover="document.querySelectorAll('.name-m').forEach(x => x.style.color='#0077B6')"
          onmouseout="document.querySelectorAll('.name-m').forEach(x => x.style.color='inherit')">永</span>)
  </h1>
</div>

<figure class="profile-photo">
  <button
    type="button"
    class="profile-photo-trigger"
    aria-label="View a larger portrait"
    aria-haspopup="dialog"
    onclick="document.getElementById('profile-photo-dialog').showModal()"
  >
    <img
      src="{{ '/assets/image/picture_260812.jpg' | relative_url }}"
      alt="Portrait of Jaeyoung Kim"
    >
  </button>
</figure>

<dialog
  id="profile-photo-dialog"
  class="profile-photo-dialog"
  aria-label="Larger portrait of Jaeyoung Kim"
>
  <form method="dialog" class="profile-photo-dialog-controls">
    <button class="profile-photo-close" aria-label="Close enlarged portrait">
      Close
    </button>
  </form>
  <a
    href="{{ '/assets/image/picture_260812.jpg' | relative_url }}"
    target="_blank"
    rel="noopener noreferrer"
    title="Open the original image"
  >
    <img
      src="{{ '/assets/image/picture_260812.jpg' | relative_url }}"
      alt="Open the original portrait in full size"
    >
  </a>
</dialog>


I am a Ph.D. student in the [Department of Mathematical Sciences](https://math.snu.ac.kr) at **Seoul National University (SNU)**, working under the supervision of [Prof. Seonhee Lim](https://sites.google.com/view/seonheelim).

<p class="contact-links">
  <span class="contact-email"><i class="fa-solid fa-envelope" aria-hidden="true"></i> <span id="contact-email" class="email-protected"></span></span>
  <noscript>Email available with JavaScript enabled.</noscript>
  <span aria-hidden="true">·</span>
  <a href="https://drive.google.com/file/d/19DYyTYiYovxxNkP_ty2DQfh6Pmn2WyXF/view?usp=sharing"
   target="_blank"
   rel="noopener noreferrer">
  <i class="fa-solid fa-file-pdf" aria-hidden="true"></i>
  Curriculum Vitae
</a>
</p>

### Research Interests

My primary research area is **Homogeneous Dynamics** of higher-rank Lie groups over real or non-Archimedean local fields, together with Ergodic Theory and Number Theory.

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
