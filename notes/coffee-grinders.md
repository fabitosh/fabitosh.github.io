---
btime: null
layout: note.njk
mtime: 2026-04-04 10:54
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
- leisure/coffee
- tech/website/hosted
title: Coffee Grinders.Md
---
## Coffee Grinders

This article assumes you have already started nerding into [[Coffee]] before. I have been looking into an upgrade of my coffee grinder. In this post I'm going through my learnings of the relevant metrics. Writing this down helps me to ensure I have understood the concepts (hopefully). This is mostly a theoretical piece. I am no taste-bud reference and have not done comparative tasting of different grinders.

Starting out, what do I want from a grinder?
- It should fit into my life: Aesthetics, Footprint, Price. Noise.
- Its grounds should allow me to brew a consistent and delicious coffee.
- The workflow with it should be enjoyable: Grind Speed. Time it takes to get a dose. Dialing in. Switching between beans. Switching between brew methods.

In the first part we'll go through the aspects of how the grinder influences the taste of the coffee. The second part was about getting clarity on the cons of using a bean-hopper, even with grind-by-weight.

Let's investigate the contributing aspects further.

### Design Goal. What kind of ground coffee will taste nice?

We need to understand what we should actually optimize for. **Particle Size Distribution (PSD)** is the basis that attempts to quantify grinder characteristics. That is, the distribution of coffee particles of different sizes. My naive assumption was always, that this is all about uniformity. My idea of an ideal grinder was one, that crushes beans into particles of equal size. The general idea is quite simple: all pieces are equally sized and can thus be equally extracted at their sweet spot. I was surprised to see, that this design target was only a rather recent thing. **Unimodal** burrs. The name hints it, we have one mode (= one particle size) where most of our particles are.
![](/assets/images/coffeegrinders-unimodal-1.png)

Traditionally, **bimodal** burrs were the norm and are still desirable due a different design goal. The underlying idea is that we have a majority of particles of "medium" size. The remaining particles should be significantly smaller bits, "filling" the space between the larger particles. Their role is to increase the overall resistance of the coffee puck.

![](/assets/images/coffeegrinders-bimodal-1.png)

There also discussions about whether multi-modal output (3+ distinct size peaks) would be desirable, though my impression was that this has still been very experimental, which I am not the target audience for in this topic. We'll thus conclude that the industry is currently on two distinct design goals discussed above.

#### Performance Quantification

How well the design goals are achieved can be quantified by how the target PSD are effectively achieved by measuring the output grounds. For unimodality, I assume this to be quite straightforward: A distinct, thin peak around one particle size. And that for all grind sizes.

> [!NOTE]  
> Generally, most find unimodal PSD desirable for filter and immersion brewing. There can be flavor preferences for more "traditional" profile with "strength". To me, that is not why one goes for filter coffee.

For bimodality, it seems a bit harder to quantify.
A low variation around the main peak would be desirable to allow the even extraction of the key tastes. This is similar to the unimodal case. For the fine particles, what would be desirable or "tasty"? Is it better to have one distinct fine particle size, or would we actually prefer them to spread over a broader particle spectrum as long as they stay far from the main peak?


#### The role of fines in espresso

Classic coffee machines ramp up to 9 bar and keep it up there until the end of the shot. To reach an extraction of the coffee, sufficient resistance needs to come from the puck. This is a primary role of the fines.
A unimodal PSD can reach the required resistance as well by grinding finer than the main peak of the main peak from the bimodal PDS. Though it is generally harder to hit that sweet spot without channeling. The fines leave a broader window to operate within.
It also would help if the machine were able to only run at a lower pressure (like 6 bars), which most machine today cannot be configured to.

Bimodal ground espresso is described to have "more body" and "creamyness". My understanding is, that this comes from fines, that are small enough that they can bass through the basket holes. These tend to stabilize coffee oils together, which is what we perceive as more "syrupy".

On the other hand unimodal PSD is said to provide "clarity". There is no over-extraction of the fines. This over-extraction tends to come with some bitterness, which disturbs said clarity. Bitterness is inherently not a bad thing, but a matter of taste. Having it in the cup might dominate or numb other flavors though.

> [!IMPORTANT]
> Higher amount of fines allow and require coarser grind settings, have "more body" and less nuanced taste profiles.

The holes in the portafilter baskets are around 200-300 $\micro m$, significantly smaller than all fines. This does not mean all fines fall through as the coffee puck provides resistance in itself. Here we start going into territory that is not straightforward I think.

> [!info]
> Permeability: Measure of how well fluids can flow through a medium

There is [Darcey's Law](https://en.wikipedia.org/wiki/Darcy%27s_law) which - applied here -describes the flow rate $Q$ through a porous medium of portafilter area $A$ and puck height $L$ as:
$$Q = \frac{\kappa A}{\micro L}\Delta P$$
$\kappa$ is the permeability, which is determined by the amount of fines and their distribution. $\micro$ is the viscosity of the coffee. Determining $\kappa$ here would require experiments, we can only formulate hypotheses here.

Overall, the only small particles metric I am interpreting is the accumulated percentage of fines in the PSD. This is not directly a quality metric, but gives an indication of how strongly a grinder leans into the traditional, "body" espresso. How much a distinct/clear main peak can compensate, I don't know.


#### Lets put some numbers to it. An example

Let's go into two simplified PSDs. They show two grinders with a dialed-in espresso.
![](/assets/images/coffeegrinders-bimodal-compare-1.png)
When it comes to the taste of the coffee, all elements are interconnected. A separation of the elements does not fully work, but it can be a helpful mental concept to understand individual contributions.
- In the chart we have the fines peak at $55\micro m$ for Grinder A and a bit lower for Grinder B. As covered in the chapter above, it will have an impact on the permeability $\kappa$ and thus the puck resistance. How, is not clear to me.
- The integral of contributions of the fines $<100\micro m$ is smaller for grinder B. Relative to grinder A, it has "less body" and produces a more nuanced shot. I am not sure whether it is harder to dial in.
- The clearer main peak helps pronounce the coffee better. More particles can be extracted at their sweet spot.
- Both grinders have their main spike at the same spot. I am not aware that anything can be derived from peak value differences.

I would expect two identical PSDs, but coming from two different grinders and burr types to taste identical, but would like to see that verified.

#### My Desire

Whilst I enjoy nerding out on coffee occasionally; in my day to day I prefer a quickly dialed in coffee and usually want the process to just work™. I think to prefer the expressive coffee notes (found with more clarity) over the more bitter aspects, but don't dislike them either.

My current machine is a quite cheap beginner model (Sage Bambino Plus) with a flat 9 bar pressure profile. I worry about not having enough controllable process parameters to pull reliable shots with changing beans. An unimodal PSD will require a significantly smaller grind size due to the absence of fines. If I were to know I could do that reliably and relative hassle-free on a day-to-day basis, I'd opt for unimodal. But, I believe that to not be the case.

This leaves me deciding between different kinds of bimodal burrs. In the discussed example above, my choice would then be grinder B.

I want my next grinder to last at least 10 years. It thus needs to provide a platform, that allows exchanging the burrs in the future.

> [!info]
> We left out quite a few, interesting aspects here. I am not questioning whether flat burrs are really better than conical ones. I think they are. Based on purely on their prevalence in high end grinders.
> The size of the burrs is not mentioned. Overall I believe that bigger burrs have a higher quality ceiling than smaller ones.
> I think the discussion is mostly relevant for light roasts. I think it is an anti-thesis to have dark roasts with a unimodal burrset.
> Lastly, the precision of the alignment of the two burr parts is fundamental for every grinder. Imperfections there will have an impact on the PSD though.

### Workflow

I needed to get clarity on the impact of a hopper in the workflow.
#### Retention
Let's start by defining retention $r$ as:
$$r_i = \text{beans}_\text{in} - \text{grounds}_\text{out}$$
We take the difference from weighted beans to ground output. $i$ is the number of the grinds since the first shot from a cleaned machine.

A clean machine has no coffee inside yet. We expect the first shots negative: $r_0=-0.1[g]$ with some coffee "filling" empty spaces and corners of the grinder. Some bits are likely going to last there until we clean the machine again. If that's the case, it does not really matter.

This brings us to the part, that I believe to be worse: The amount of coffee staying in the grinder and coming out with the next grind. This could be stale coffee from 3 days ago (if we have not used the machine over the weekend). Or ground coffee from a different brewing method before.

![](/assets/images/coffeegrinders-retention-1.png)

I propose we name the two types of retention:
- Fixed retention: coffee stuck in the grinder, but not moving
- Exchanged retention

##### Measuring
How do we measure the two?

I would imagine the fixed retention to slowly build up in reality. Measuring it should be easy: Clean the grinder thoroughly after some usage. Measure all coffee you cleaned out of the machine.

Exchanged rotation is likely more nuanced. We could color the beans for each dose and see how much of the last color comes out? This might already work when swapping from light to dark roast.

One can also measure the weight consistency. What variance do our retention measurements $r_i$ have? In other words, measuring the exchanged retention consistency. That is helpful. If we consistently get $r=0$, we can trust we are working with the same weight in each shot at least. My impression is that many reviewers measure that number. It's important to remember, that this is not the same as the exchanged retention.
##### Does exchanged retention even matter?

The interest or almost obsession with retention is a newer thing with the rise of home baristas. In an industrial setting, a grinder gets dialed in and pulls likely a few hundred shots with the same coffee bean and grind size. The included exchanged retention will still be fresh and in of the same target size.

My use-case is different. There are stretches of days without me making a coffee at home. Meaning the first shot after this period would contain old coffee.
Or I might want to do a filter coffee in the morning and have an espresso after lunch. The filter-sized grounds should not land in the portafilter.
Both issues can be mitigated by a purging the estimated exchanged retention initially.

#### Single-Dosing vs Grind-By-Weight

So far, we assumed pre-weighting the beans before every shot. Coffee hoppers aim to speed up that workflow. We can time how long we rotate the burrs and use that as a dosing proxy. This is quite consistent in an established recipe. But falls short as soon as we change the grind size or beans. Coarser grind settings will produce more coffee in the same time interval.

Grind-By-Weight addresses this issue by directly measuring the amount of coffee at the output and introducing a smarter control-loop. Overall, that's pretty cool and handy.

My issue with both of those methods is, that for both of them to work we need a continuous stream of coffee beans as input. This comes with significantly more exchanged retention. Some of the exchanged retention is in half-crushed bean-state. The ones that were just in between the burrs when the control-loop

![](/assets/images/coffeegrinders-hopperretention-1.png)


Again, we can mitigate by more purging. Or alternatively, just embrace the Frankenstein Shots. To dial in espresso I would switch to single dosing until the right setting is found. Then set the target time/weight that matches the determined recipe.

I'm currently having a grinder with hopper and grind-by-time. I started using it as a single-dose hopper. Overall, I find it less cumbersome pre-weighting the beans than I expected. I currently have a dedicated hand grinder for the filter coffee. My next grinder should be able to handle both filter and espresso. In that scenario single-dosing seems more convenient to me.

### Wrapping it up

I am looking for a single-dose grinder with low exchanged rotation. Whilst uniform burrs likely would match my taste preference, I don't trust it to be hassle-free enough on my flat 9-bar coffee machine.


[[Concrete Coffee Grinder Comparisons]]