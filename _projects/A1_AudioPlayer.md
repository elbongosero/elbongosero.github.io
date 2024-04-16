---
layout: page
title: A1 Audios 
description: Three Random Repetitions, P1-P4
img: 
importance: 1
category: Audios
---
   
   
   ----

   # Audio Player 

   ----


{% assign myPath = "_projects/assets/audios/A1" %}
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


{% for x in (0..23) %}
{% assign path = site.baseurl | append: "/explore/assets/audios/A1/" | append: folderList[x] %}
<table>
<br><br>
<p><strong>{{folderList[x]}}</strong></p>
<audio controls><source src="{{ path | append: "/original.mp3" }}"></audio>

  <thead>
    <tr>
      <th> </th>
      <th>Rep 0</th>
      <th>Rep 1</th>
      <th>Rep 2</th>
    </tr>
  </thead>
  <tbody>
    
    <tr>
      <td>P1</td>
      <td><audio controls><source src="{{ path | append: "/Participant_1_repetition_0.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_1_repetition_1.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_1_repetition_2.mp3" }}"></audio></td>

    </tr>

    <tr>
      <td>P2</td>
      <td><audio controls><source src="{{ path | append: "/Participant_2_repetition_0.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_2_repetition_1.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_2_repetition_2.mp3" }}"></audio></td>

    </tr>
    
    <tr>
      <td>P3</td>
      <td><audio controls><source src="{{ path | append: "/Participant_3_repetition_0.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_3_repetition_1.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_3_repetition_2.mp3" }}"></audio></td>

    </tr>

    <tr>
      <td>P4</td>
      <td><audio controls><source src="{{ path | append: "/Participant_4_repetition_0.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_4_repetition_1.mp3" }}"></audio></td>
      <td><audio controls><source src="{{ path | append: "/Participant_4_repetition_2.mp3" }}"></audio></td>

    </tr>
    
  </tbody>
</table>
{% endfor %}
