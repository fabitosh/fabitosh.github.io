---
layout: layout.njk
title: fabio.earth - notes
---

# Notes

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Created</th>
      <th>Modified</th>
    </tr>
  </thead>
  <tbody>
  {%- for note in collections.notes -%}
    <tr>
      <td>
        <a href="{{ note.url }}">{{ note.data.title }}</a>
        {%- if note.data.tags -%}
          <span class="tags">
          {% for tag in note.data.tags %} <span class="tag">{{ tag }}</span> {% endfor %}
          </span>
        {%- endif -%}
      </td>
      <td><small>{{ note.data['btime'] | date: "%Y-%m-%d" }}</small></td>
      <td>
        {%- if note.data['mtime'] -%}
          <small>{{ note.data['mtime'] | date: "%Y-%m-%d" }}</small>
        {%- else -%}
          <small>-</small>
        {%- endif -%}
      </td>
    </tr>
  {%- endfor -%}
  </tbody>
</table>