---
layout: page
title: LogBook
permalink: /logbook/
published: true
---
A series of logs about my work. Hopefully on daily bases.

<h2>Logs Index</h2>
<ul>
  {% for log in site.logsfiles %}
    <li>
      <a href="{{ log.url }}">{{ log.title | default: log.path }}</a>
    </li>
  {% endfor %}
</ul>

