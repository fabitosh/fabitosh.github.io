---
layout: layout.njk
title: fabio.earth - notes
---

# Notes

<ul>
  {% for note in collections.notes %}
    <li><a href="{{ note.url }}">{{ note.data.title }}</a></li>
  {% endfor %}
</ul>
