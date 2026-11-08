---
description: "Why Training for the Uphill Athlete convinced me I had Aerobic Deficiency Syndrome (ADS), and why I stopped following its Zone 2 dogma after two weeks."
btime: 2026-11-08
layout: note.njk
mtime: null
permalink: notes/{{ page.fileSlug }}/index.html
status: completed
tags:
  - sport
  - book notes
title: Aerobic Deficiency "Syndrome"
---

Over the past seven years I have been a pretty consistent, albeit lower-volume endurance athlete. On average I recorded 350h of moving activity per year (6:43h/week). Mostly running and cycling. Also mostly unstructured and for fun. Performance is of course a broad spectrum. With races in the range of a 1:25h half marathon (2022), a 37:33 10k (2024), and an estimated FTP of ~300W (4.2 W/kg), I always thought my aerobic fitness should be alright.
The book _Training for the Uphill Athlete_ made me question that. Do I have _Aerobic Deficiency Syndrome (ADS)_? And if so, should I care?

## Zones?

I understood the need to determine my maximum heart rate (HR) and not rely on the 220 minus age "rule". Luckily. My max HR is ~205, whereas the "rule" would set it at 186. Still, I felt like it was a fair bet to base my effort zones off my maximum HR. The zones attempt to categorize how hard we are going. Different zone categorizations exist, yet the key parameters around them are:

- AeT: Aerobic Threshold
- AnT: Anaerobic Threshold

The 5-zone system found on Strava and Garmin follows 1 < 2 up to AeT < 3 < 4 up to AnT < 5. You'll find a plethora of articles on this topic elsewhere if you want to read up more on it.

<figure>
<svg viewBox="0 0 610 115" role="img" aria-label="5-zone heart rate scale from 110 to 205 bpm showing Z1, Z2 up to AeT at 170 bpm, Z3, Z4 up to AnT at 189 bpm, and Z5 up to 205 bpm" style="display:block; width:100%; max-width:610px; margin:0 auto; font-family:inherit">
  <!-- Threshold markers above bar -->
  <g stroke="currentColor" stroke-width="1.5">
    <line x1="380" y1="26" x2="380" y2="82" stroke-dasharray="3,3"/>
    <line x1="494" y1="26" x2="494" y2="82" stroke-dasharray="3,3"/>
    <line x1="590" y1="26" x2="590" y2="82" stroke-opacity="0.5"/>
  </g>
  <g fill="currentColor" font-size="12" text-anchor="middle">
    <text x="380" y="14" font-weight="bold">AeT (~170)</text>
    <text x="494" y="14" font-weight="bold">AnT (~189)</text>
    <text x="590" y="14" text-anchor="end" opacity="0.75">Max (~205)</text>
  </g>
  <!-- Zone bar (110 to 205 bpm, 6px per bpm) -->
  <g stroke="currentColor" stroke-width="1.2">
    <rect x="20" y="36" width="210" height="36" rx="4" fill="currentColor" fill-opacity="0.06"/>
    <rect x="230" y="36" width="150" height="36" fill="currentColor" fill-opacity="0.14"/>
    <rect x="380" y="36" width="60" height="36" fill="currentColor" fill-opacity="0.24"/>
    <rect x="440" y="36" width="54" height="36" fill="currentColor" fill-opacity="0.34"/>
    <rect x="494" y="36" width="96" height="36" rx="4" fill="currentColor" fill-opacity="0.46"/>
  </g>
  <!-- Zone labels inside bar -->
  <g fill="currentColor" font-size="13" font-weight="bold" text-anchor="middle">
    <text x="125" y="59">Z1</text>
    <text x="305" y="59">Z2</text>
    <text x="410" y="59">Z3</text>
    <text x="467" y="59">Z4</text>
    <text x="542" y="59">Z5</text>
  </g>
  <!-- BPM ticks below bar -->
  <g fill="currentColor" font-size="11" opacity="0.7" text-anchor="middle">
    <text x="20" y="98" text-anchor="start">110 bpm</text>
    <text x="230" y="98">145</text>
    <text x="380" y="98">170</text>
    <text x="440" y="98">180</text>
    <text x="494" y="98">189</text>
    <text x="590" y="98" text-anchor="end">205</text>
  </g>
</svg>
<figcaption>My initial HR-derived 5-zone setup, with AeT around 170 bpm and AnT around 189 bpm.</figcaption>
</figure>

### Where does my Z2 end? (AeT)

_The Uphill Athlete_ focuses primarily on the AeT. It suggests a proxy that one is below AeT when one can comfortably breathe through the nose. This really got me off-path into a rabbit hole. For two weeks I believed myself to be aerobically deficient.

I can only breathe comfortably through my nose until about 135bpm. With my believed AeT at 170bpm, this was extremely off. I knew it was a rough proxy, but being that far off must still mean something, right? My drift test (run two identical loops of ~30mins below assumed AeT at a steady HR; if pace-to-HR drift stays within 5%, you were below AeT) reaffirmed that. Yet, there I screwed up by accidentally using my wrist HR and not realizing that the external HR monitor was off.

<figure>
<svg viewBox="0 0 610 125" role="img" aria-label="Zone shift under the nasal breathing test: AeT drops to 135 bpm, leaving a massive 54 bpm gap to AnT at 189 bpm" style="display:block; width:100%; max-width:610px; margin:0 auto; font-family:inherit">
  <!-- Threshold markers -->
  <g stroke="currentColor" stroke-width="1.5">
    <line x1="170" y1="26" x2="170" y2="90" style="stroke: var(--pico-primary, currentColor)"/>
    <line x1="380" y1="26" x2="380" y2="90" stroke-dasharray="2,4" stroke-opacity="0.45"/>
    <line x1="494" y1="26" x2="494" y2="90" stroke-dasharray="3,3"/>
  </g>
  <g fill="currentColor" font-size="12" text-anchor="middle">
    <text x="170" y="14" font-weight="bold" style="fill: var(--pico-primary, currentColor)">Nasal AeT (135)</text>
    <text x="380" y="14" opacity="0.5">Believed AeT (170)</text>
    <text x="494" y="14" font-weight="bold">AnT (~189)</text>
  </g>
  <!-- Bar -->
  <g stroke="currentColor" stroke-width="1.2">
    <rect x="20" y="36" width="150" height="36" rx="4" fill="currentColor" fill-opacity="0.12"/>
    <rect x="170" y="36" width="324" height="36" fill="currentColor" fill-opacity="0.28" style="stroke: var(--pico-primary, currentColor)"/>
    <rect x="494" y="36" width="96" height="36" rx="4" fill="currentColor" fill-opacity="0.46"/>
  </g>
  <!-- Labels inside bar -->
  <g fill="currentColor" font-size="12" text-anchor="middle">
    <text x="95" y="59" font-weight="bold">Z1–Z2 (≤135)</text>
    <text x="332" y="53" font-weight="bold">Z3–Z4 (~29% spread to AnT)</text>
    <text x="332" y="67" font-size="10.5" opacity="0.8">"off-limits" during base phase</text>
    <text x="542" y="59" font-weight="bold">Z5</text>
  </g>
  <!-- BPM ticks -->
  <g fill="currentColor" font-size="11" opacity="0.7" text-anchor="middle">
    <text x="20" y="106" text-anchor="start">110 bpm</text>
    <text x="170" y="106" font-weight="bold" style="fill: var(--pico-primary, currentColor)">135</text>
    <text x="380" y="106" opacity="0.6">170</text>
    <text x="494" y="106">189</text>
    <text x="590" y="106" text-anchor="end">205</text>
  </g>
</svg>
<figcaption>What the nasal breathing proxy (~135 bpm) implied: tiny Z1–Z2 and a massive ~29% gap to AnT.</figcaption>
</figure>

In the sections on building up one's training plan, I was also faced with a further indication of being aerobically insufficient:

> Athletes in need of building a base: Have not averaged more than 400 hours per year of focused training for running or skimo during the past two years.

With me only having had one year of 400+ logged hours and their base phase implying no training above Z2... Well, that should explain things, right?

I was wrong. What got me back on track was a friend pushing back on my book-inspired wild claims. I did not feel like spending ~300 CHF for a one-time lactate test (a more reliable method that the book also mentions). What other ways to estimate my blood-lactate levels exist? I stumbled onto how heart rate variability (HRV) data can be tracked not only overnight, but also during activity. Specifically using a metric called DFA $\alpha_1$ (detrended fluctuation analysis). As intensity increases, the nervous system shifts from parasympathetic to sympathetic dominance, causing HRV (and DFA $\alpha_1$) to drop predictably across the aerobic and anaerobic (ventilatory) thresholds. I plan on writing more about this in an upcoming project. In short, this was finally a measurement that disagreed with my AeT being criminally low. With that, I dug deeper, realized my first drift test had used unreliable wrist data instead of my chest strap, and redid it properly. Both the new drift test and DFA $\alpha_1$ agreed: the nasal breathing test was just a blatant false positive.

### Frustration with the book

Finding out that my estimated AeT is effectively around 167bpm—roughly back in the initial max-HR ballpark, and ~12% off my AnT—was a relief. Yet even with those numbers, the book prescribes training exclusively below AeT until it sits within 10% of AnT. That made me realize I fundamentally disagree with its prescription.

<figure>
<svg viewBox="0 0 610 125" role="img" aria-label="Estimated AeT at 167 bpm: 12% spread to AnT at 189 bpm, right next to the book's 10% base-building cutoff" style="display:block; width:100%; max-width:610px; margin:0 auto; font-family:inherit">
  <!-- Threshold markers -->
  <g stroke="currentColor" stroke-width="1.5">
    <line x1="170" y1="26" x2="170" y2="90" stroke-dasharray="2,4" stroke-opacity="0.4"/>
    <line x1="362" y1="26" x2="362" y2="90" style="stroke: var(--pico-primary, currentColor)"/>
    <line x1="494" y1="26" x2="494" y2="90" stroke-dasharray="3,3"/>
  </g>
  <g fill="currentColor" font-size="12" text-anchor="middle">
    <text x="170" y="14" opacity="0.5">Nasal (135)</text>
    <text x="362" y="14" font-weight="bold" style="fill: var(--pico-primary, currentColor)">Estimated AeT (~167)</text>
    <text x="494" y="14" font-weight="bold">AnT (~189)</text>
  </g>
  <!-- Bar -->
  <g stroke="currentColor" stroke-width="1.2">
    <rect x="20" y="36" width="210" height="36" rx="4" fill="currentColor" fill-opacity="0.06"/>
    <rect x="230" y="36" width="132" height="36" fill="currentColor" fill-opacity="0.16" style="stroke: var(--pico-primary, currentColor)"/>
    <rect x="362" y="36" width="132" height="36" fill="currentColor" fill-opacity="0.28"/>
    <rect x="494" y="36" width="96" height="36" rx="4" fill="currentColor" fill-opacity="0.46"/>
  </g>
  <!-- Labels inside bar -->
  <g fill="currentColor" font-size="12" text-anchor="middle">
    <text x="125" y="59" font-weight="bold">Z1</text>
    <text x="296" y="59" font-weight="bold">Z2 (up to ~167)</text>
    <text x="428" y="53" font-weight="bold">Z3–Z4 (~12%)</text>
    <text x="428" y="67" font-size="10.5" opacity="0.8">&gt;10% = base building</text>
    <text x="542" y="59" font-weight="bold">Z5</text>
  </g>
  <!-- BPM ticks -->
  <g fill="currentColor" font-size="11" opacity="0.7" text-anchor="middle">
    <text x="20" y="106" text-anchor="start">110 bpm</text>
    <text x="170" y="106" opacity="0.5">135</text>
    <text x="230" y="106">145</text>
    <text x="362" y="106" font-weight="bold" style="fill: var(--pico-primary, currentColor)">167</text>
    <text x="494" y="106">189</text>
    <text x="590" y="106" text-anchor="end">205</text>
  </g>
</svg>
<figcaption>My estimated AeT (~167 bpm): roughly back in the initial ballpark, yet at ~12% off AnT (&gt;10%) the book still prescribes pure base building.</figcaption>
</figure>

To me, cutting out all higher-intensity work seems highly wasteful for people with an already well-trained anaerobic pathway. I see the argument for focusing on the aerobic side, and the book argues nicely how training one pathway comes at the cost of the other through the concepts of capacity and utilization training. However, it entirely leaves out that maintaining a capability is significantly easier than building it up. Omitting paces near race effort also compromises muscular and tendon stiffness (running economy). Under _The Uphill Athlete_'s logic, you essentially don't get to race at all until you have finished building that base. I think it's fair to consider a regular marathon an endurance event, and it is run almost exclusively in a Z3/Z4 range. No performance-oriented marathon training plan I found suggests Z2 only. They all emphasize how important the structural adaptation to the continuous leg beating at pace is and incorporate significant blocks around threshold. I am aware that trail runs can be substantially longer, but they certainly aren't all.

This brings me to my broader criticism of the book's tone. The need for the two thresholds to be that close is overstated, and slapping a medical label like "syndrome" onto a normal, training-history-related adaptation feels icky. I see the marketing appeal: it's catchy, triggers fear, and suggests a condition that needs treatment. It certainly worked on me for two weeks. Yet it simply pathologizes something normal and oversimplifies something complex. Unsurprisingly, that philosophy can be further "honed" through their coaching sold under a similar name. The book's overall methodology is probably more sound if you only intend on racing for over 6 hours. For me, 5k races (still ~90% aerobic) and marathons are definitely part of my interest.

Throughout the book, I also kept coming back to one key blind spot: what if I am not recovery-limited, but time-limited? The book treats Z3 (slightly above AeT) as a "black hole" to be avoided at all costs whilst we are so aerobically sick, even though the aerobic system is still heavily trained there. There lies a key difference in the book [Norwegian Singles Method: Subthreshold Running Kept Simple](https://www.goodreads.com/book/show/239471190-norwegian-singles-method). It treats the runner's time restriction as a core constraint. It recognizes the untapped aerobic potential in most non-elites as well, but does not neglect sub-threshold efforts. It actually suggests them as a key way to improve performance. I would definitely recommend that one instead if you have a similar focus to mine.

In short, don't fall for the uphill cult like I initially did.
