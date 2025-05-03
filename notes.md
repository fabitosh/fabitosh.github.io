---
layout: layout.njk
title: fabio.earth - notes
---

# Notes

<table class="table table-sm table-hover align-middle">
  <thead class="table-light">
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
          <span class="ms-2">
          {% for tag in note.data.tags %} <span class="badge rounded-pill text-bg-light fw-normal me-1">{{ tag }}</span> {% endfor %}
          </span>
        {%- endif -%}
      </td>
      <td class="text-muted small">{{ note.date | date: "%Y-%m-%d" }}</td>
      <td>
        {%- if note.data['date modified'] -%}
          <span class="text-muted small">{{ note.data['date modified'] | date: "%Y-%m-%d" }}</span>
        {%- else -%}
          <span class="text-muted small">-</span>
        {%- endif -%}
      </td>
    </tr>
  {%- endfor -%}
  </tbody>
</table>