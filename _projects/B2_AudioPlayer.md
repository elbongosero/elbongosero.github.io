---
layout: page
title: B2 Audios 
description: Simple/Complex, P1 Only
img: 
importance: 1
category: Audios
---
   
   
   ----

   # Audio Player 

   ----


{% assign myPath = "_projects/assets/audios/B2" %}
{% assign folderList = "" | split: "," %}

{% for file in site.static_files %}
  {% if file.path contains myPath %}
    {% assign filePathParts = file.path | split: "/" %}
    {% assign folderName = filePathParts[4] %}
    {% unless folderList contains folderName %}
      {% assign folderList = folderList | push: folderName %}
    {% endunless %}
  {% endif %}
{% endfor %}


{% assign folderList = folderList | sort %}




<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid black;
  padding: 4px;
  text-align: center;
  width: 10%;
}

th {
  background-color: lightgray;
}
</style>


{% for x in (0..203) %}
{% assign path = site.baseurl | append: "/explore/assets/audios/B2/" | append: folderList[x] %}
<table>
<br><br>
<p><strong>{{folderList[x]}}</strong></p>
<audio controls><source src="{{ path | append: "/original.mp3" }}"></audio>

  <thead>
    <tr>
      <th> </th>
      <th>Simple</th>
      <th>Complex</th>
    </tr>
  </thead>
  <tbody>
    
    <tr>
      <td>P1</td>
      <td><audio controls><source src="{{ path | append: "/Participant_1_simple.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_1_complex.mp3" }}"></audio></td>


    </tr>
  
    
  </tbody>
</table>
{% endfor %}
