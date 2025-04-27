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
          <span class="tags-inline">
          {% for tag in note.data.tags %}<span class="tag">{{ tag }}</span> {% endfor %}
          </span>
        {%- endif -%}
      </td>
      <td>{{ note.date | date: "%Y-%m-%d" }}</td>
      <td>
        {%- if note.data['date modified'] -%}
          {{ note.data['date modified'] | date: "%Y-%m-%d" }}
        {%- else -%}
          -
        {%- endif -%}
      </td>
    </tr>
  {%- endfor -%}
  </tbody>
</table>

<style>
table {
  border-collapse: separate;
  margin-top: 1em;
}

th, td {
  padding: 0.5em;
  text-align: left;
  vertical-align: top;
  border-bottom: 1px solid #eee;
}

th {
  background-color: #f8f8f8;
  font-weight: bold;
}

.tags-inline {
  margin-left: 0.5em;
}

.tag {
  display: inline;
  background-color: transparent;
  border: 1px solid #ddd;
  padding: 0.1em 0.3em;
  border-radius: 3px;
  font-size: 0.8em;
  margin-right: 0.2em;
  color: #555;
  white-space: nowrap;
}
</style>