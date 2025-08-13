---
layout: default
title: Wåndyr Interactive
---

<div class="container">
  <p>
    <img
      src="images/wilderland.jpg"
      style="width: 100%"
      alt="Wilderland landscape"
    />
  </p>

  <div class="jumbotron">
    <h1>Wåndyr</h1>
    <p class="lead">
      Wåndyr is an adventure game inspired by the original roleplaying games
      but updated with fresh game mechanics. The game fits in a small 20
      page booklet. Read this first.
    </p>
    <p>
      <a href="docs/Wåndyr, an Adventure Game v0.5.pdf" target="_blank"
        >Wåndyr, an Adventure Game</a
      >
    </p>
  </div>

  <div class="jumbotron">
    <h1>Game Summary</h1>
    <p class="lead">
      Wåndyr is an adventure game about a band of adventurers wandering through a pulp fantasy world. The focus is on exploration, following rumors, discovering new places, finding magic, treasure hunting, camping, singing, storytelling, cleverly overcoming impossible odds, and coming back alive with tales to tell.
    </p>
    <p>
      In the spirit of The Hobbit, Wåndyr celebrates the journey of going there and back again. The stories and songs of your characters emerge during play, filled with wonder and surprises that even the Guide doesn't anticipate. The game starts in an undefined "wilderland" that emerges during play, which you can optionally place somewhere in the fantasy world of your choice.
    </p>
    <h3>Key Features</h3>
    <ul>
      <li><strong>Sandbox Style:</strong> The Guide describes the world but doesn't create a story beforehand. Each new discovery adds to the growing lore of your campaign world.</li>
      <li><strong>Simple Characters:</strong> Each character has two Traits and two Skills, making it quick to create and easy to play.</li>
      <li><strong>The Oracle:</strong> A unique system that answers yes/no questions instantly, often adding unexpected "sweet" or "spicy" flavor to keep adventures surprising.</li>
      <li><strong>OSR Compatible:</strong> Works with most Old School Roleplaying games while offering fresh mechanics.</li>
    </ul>
  </div>

  <div class="jumbotron">
    <h1>The Oracle</h1>
    <p>
      The Oracle is a simple but powerful system for answering questions during play. Roll 2d6: if the total is 8 or higher, the answer is "Yes"; otherwise, it's "No". Questions should be phrased so that characters want to hear "Yes", like "Do we find shelter?" or "Is the sword magical?"
    </p>
    <p>
      The Oracle adds flavor through "Sweet" and "Spicy" results. Roll a 6 on either die for a "Sweet" result, or a 1 for a "Spicy" result. On Sweet, the player asks a follow-up question; on Spicy, the Guide asks a question. The Oracle also excels at playing "20 questions" to reveal mysteries piece by piece.
    </p>
    <p>
      The Wåndyr World Oracle is a set of useful random tables to help generate the wilderland setting. Both Guide and players can use these tables to discover what lies beyond the next hill or behind the next door.
    </p>
    <p>
      <a href="docs/Wåndyr World Oracle.pdf" target="_blank"
        >Wåndyr World Oracle</a
      >
    </p>
  </div>

  <!-- Interactive Tools Section -->
  <div class="tools-section">
    <h2>Game Tools</h2>
    
    <!-- Insight Spinner -->
    <div class="card mb-4">
      <div class="card-body">
        <h3>Insight Roller</h3>
        <p>Roll for Insight to claim advantage. Roll d6 each Turn.</p>
        <div class="slot-machine" id="insightSlot">
          <div class="reel">
            <div class="reel-strip" id="reel1">
              <div class="reel-item">TRAIT</div>
              <div class="reel-item">ITEM</div>
              <div class="reel-item">SKILL</div>
              <div class="reel-item">NAME</div>
              <div class="reel-item">ASSIST</div>
              <div class="reel-item">EFFORT</div>
              <div class="reel-item">TRAIT</div>
              <div class="reel-item">ITEM</div>
              <div class="reel-item">SKILL</div>
            </div>
          </div>
          <div class="reel">
            <div class="reel-strip" id="reel2">
              <div class="reel-item">TRAIT</div>
              <div class="reel-item">ITEM</div>
              <div class="reel-item">SKILL</div>
              <div class="reel-item">NAME</div>
              <div class="reel-item">ASSIST</div>
              <div class="reel-item">EFFORT</div>
              <div class="reel-item">TRAIT</div>
              <div class="reel-item">ITEM</div>
              <div class="reel-item">SKILL</div>
            </div>
          </div>
          <div class="reel">
            <div class="reel-strip" id="reel3">
              <div class="reel-item">TRAIT</div>
              <div class="reel-item">ITEM</div>
              <div class="reel-item">SKILL</div>
              <div class="reel-item">NAME</div>
              <div class="reel-item">ASSIST</div>
              <div class="reel-item">EFFORT</div>
              <div class="reel-item">TRAIT</div>
              <div class="reel-item">ITEM</div>
              <div class="reel-item">SKILL</div>
            </div>
          </div>
        </div>
        <div class="result-display" id="insightResult">
          Roll for Insight...
        </div>
        <button class="btn-roll" onclick="rollInsight()">Roll Insight</button>
      </div>
    </div>

    <!-- Oracle Dice -->
    <div class="card">
      <div class="card-body">
        <h3>Oracle Roller</h3>
        <p>Roll 2d6 for the Oracle. 8+ is "Yes", otherwise "No". Roll a 6 for "Sweet" or 1 for "Spicy".</p>
        <div class="dice-tray" id="diceTray">
          <div class="dice" id="dice1">
            <div class="dice-face">1</div>
            <div class="dice-face">2</div>
            <div class="dice-face">3</div>
            <div class="dice-face">4</div>
            <div class="dice-face">5</div>
            <div class="dice-face">6</div>
          </div>
          <div class="dice" id="dice2">
            <div class="dice-face">1</div>
            <div class="dice-face">2</div>
            <div class="dice-face">3</div>
            <div class="dice-face">4</div>
            <div class="dice-face">5</div>
            <div class="dice-face">6</div>
          </div>
        </div>
        <div class="result-display" id="oracleResult">
          Roll the Oracle...
        </div>
        <button class="btn-roll" onclick="rollOracle()">Roll Oracle</button>
      </div>
    </div>
  </div>

  <!-- Tables Section - Automatically Generated -->
  <div class="jumbotron">
    <h1>Random Tables & Oracles</h1>
    <p class="lead">
      Browse and use the extensive collection of random tables for worldbuilding, encounters, and adventure generation.
    </p>
    
    <div class="tables-grid">
      {% for table in site.tables %}
        <div class="table-card">
          <span class="table-category">{{ table.category | default: 'Table' }}</span>
          <h3>{{ table.title }}</h3>
          {% if table.description %}
            <p>{{ table.description }}</p>
          {% endif %}
          <a href="{{ table.url }}" class="btn-roll">View Table</a>
        </div>
      {% endfor %}
    </div>
  </div>

  <div class="jumbotron">
    <h1>AI Play</h1>
    <p class="lead">
      Wåndyr is primarily a tabletop roleplaying game, designed for pencils,
      paper, and friends around a table. However, it also works well with AI
      tools, both for generating content and for solo play.
    </p>

    <p>
      Wåndyr has its own approach to spellcasting, but is compatible with
      spells from the original roleplaying game and similar. The Magic
      Oracle is an AI prompt to help the Guide generate spells and
      spellbooks.
    </p>
    <p>
      <a href="docs/Wåndyr Magic Oracle.pdf" target="_blank"
        >Wåndyr Magic Oracle</a
      >
    </p>
    <p>
      Nobody available this week? Wåndyr also works well for AI solo play.
      Create a new AI project, add the game rules and world oracle, and use
      this prompt to generate your adventure.
    </p>
    <p>
      <a href="docs/Wåndyr AI Solo Play.pdf" target="_blank"
        >AI Prompt for AI Solo Play</a
      >
    </p>
  </div>

  <div class="jumbotron">
    <h1>Version History</h1>
    <p>
      <a href="docs/Wåndyr Version History v0.5.pdf" target="_blank"
        >Version History</a
      >
    </p>
    <p>
      <a href="docs/Wåndyr, an Adventure Game v0.5.pdf" target="_blank"
        >Wåndyr v0.5</a
      > (May 2025)
    </p>
    <p>
      <a href="docs/Wåndyr, an Adventure Game v0.2.pdf" target="_blank"
        >Wåndyr v0.2</a
      > (February 2025)
    </p>
    <p>
      <a href="docs/Wåndyr, an Adventure Game v0.1.pdf" target="_blank"
        >Wåndyr v0.1</a
      > (January 2025)
    </p>
  </div>

  <footer class="text-center">
    <p>Copyright © 2025 Paul Abrams</p>
    <p>
      All rights reserved. No part of this work may be reproduced or
      transmitted in any form or by any means whatsoever without express
      written permission from the author, except in the case of brief
      quotations embodied in critical articles and reviews. Please refer all
      pertinent questions to the publisher.
    </p>
  </footer>
</div> 