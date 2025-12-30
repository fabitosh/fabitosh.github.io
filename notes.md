---
layout: layout.njk
title: fabio.earth - notes
permalink: /
---

# Notes

<div>
{%- for note in collections.notes -%}
    <hgroup>
      <h2><a href="{{ note.url }}">{{ note.data.title }}</a>
        {%- if note.data.tags -%}
          {% for tag in note.data.tags %} <span class="tag">{{ tag }}</span> {% endfor %}
        {%- endif -%}</h2>
      <p>
        {{ note.data['btime'] | date: "%Y-%m-%d  " }}
        {%- if note.data['mtime'] -%}
          | last updated {{ note.data['mtime'] | date: "%Y-%m-%d" }}
        {%- endif -%}
      </p>
    </hgroup>
{%- endfor -%}
</div>
