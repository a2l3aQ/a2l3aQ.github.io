---
layout: base
title: Alle Posts
permalink: /_posts/
---

<h1>Alle Posts</h1>

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <small>{{ post.date | date: "%Y-%m-%d" }}</small>
  </li>
{% endfor %}
</ul>
