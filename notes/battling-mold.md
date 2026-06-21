---
btime: 2026-06-20 15:46
layout: note.njk
mtime: null
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
  - thermodynamics
title: Battling Mold
---

My girlfriend is struggling with high humidity and resulting mold in her apartment.
Time to pull out the old thermodynamics class notes and attack it full force.

## Assessing the Situation

Some of what I consider relevant facts:

- Over the past years, she has seen mold growing at the bottom of some corners.
- The problem was always prevalent during winter, but never started in the summer.
- Despite having gotten it professionally removed, it reappeared the next winter.
- The apartment is on the ground floor.
- Her humidity sensors are often reaching 70% relative humidity.
- Her neighbours are reporting similar problems.

This likely sounds familiar to many with a mold problem.

## Mold

Mold can grow on almost any substance when moisture is present. To flourish and grow, it needs nutrients (such as cellulose, found in walls) and time.
Realistically, we'll only be able to battle the moisture. She wouldn't like me if I tore down her walls.

Mold is bad. It looks ugly, destroys the walls over the longer term and has bad effects on your health.

Moisture could come from water/pipe leakages. That would need a fix at the source.
We hope her excess moisture does not come from the ground up into the walls. This would be a lost battle as the water source is way larger than any ability to remove it through the air.

## Don't be like water, fight it

When you shower hot for a while, the entire bathroom will likely be moist. There, you might have heard of the importance to open the window to air it out.

In general, common wisdom is to open the windows frequently (say 2-4 times a day) for short durations and "exchange" all air - especially if you are battling mold. Why is that? What underlying physical properties help it? How effectively are you tackling the problem with it?

How much would a dehumidifier help?

## Let's get nerdy: Psychrometrics

> [!NOTE]
> Psychrometrics is the engineering discipline concerned with the properties of gas-vapor mixtures.

We are jumping straight in.
Let's clarify two concepts:

- Saturation: The point where a volume of air cannot contain more water without forming drops.
- Relative Humidity: $\frac{\text{water in the air}}{\text{water of saturation point}}$

This at first overwhelming [chart](https://www.flycarpet.net/en/psyonline) below is awesome as it contains all hard numbers we need:

![Psychrometric chart plotting humidity ratio against temperature, with red relative-humidity curves and blue specific-volume lines](/assets/images/battling-mold-psychrometric-chart.png)

Let me guide you through it:

- Horizontal axis (x): temperature as measured by our regular thermostat
- Right vertical axis (y): Humidity Ratio $W$. g of water vapor per kg of dry air
  - We can see that this tops out in a curve until it gets cut off at ~32 degrees Celsius. This topping out is when the air is fully saturated. Our relative humidity is reaching 100%. This is exactly when we get moisture. We can see other relative humidity lines in red. This is a key dynamic to understand for our indoor mold problem. We'll come back to it.
  - Above 32 degrees, the graph is directly horizontal. This is not due to a physical phenomenon, but the graph just cutting off.
- Blue dashed diagonal lines: Specific Volume ($[m^3 / (\text{kg of dry air})]$)
- Pressure is constant at 1 bar / atmospheric pressure. This is sufficient for our use-case. In general, that is one more dimension to consider.

The key qualitative message is:

> [!IMPORTANT]
> Air at a higher temperature can carry significantly more water than the one at a lower temperature. A temperature reduction can lead to moisture.

The effective numbers help us quantify the humidity problem in the apartment.

Let's use this knowledge to answer our first question:

### Should I open the windows?

Does opening the windows make sense when our goal is to reduce humidity levels?
We start by plugging in our relevant numbers.

#### Quantifying the humidity loss

We have measured indoor temperature and relative humidity. On average they are
$T_i = 22$, $RH_i = 70\%$

Outdoors, that varies a bit more. Let's pull some information from [meteoschweiz.admin.ch](https://www.meteoschweiz.admin.ch/service-und-publikationen/applikationen/messwerte-und-messnetze.html#param=messwerte-luftfeuchtigkeit-10min&table=false&station=SMA&chart=day) for the Meteo station in Zürich, Fluntern.
![Daily mean outdoor temperature in Zürich Fluntern over a year, ranging from near 0°C in winter to about 25°C in summer](/assets/images/battling-mold-meteo-zurich-temperature.png)

![Daily mean outdoor relative humidity in Zürich Fluntern over a year, mostly between 60% and 100%](/assets/images/battling-mold-meteo-zurich-humidity.png)

I'd say the following values are fair averages for winter months

$T_o=3$ $RH_o = 85\%$

How does the water mass change if we exchange one cubic meter ($m^3$) of air from outdoors with the one indoors?
$$\Delta m_\text{Water} = \Delta m_\text{dry air} \times (W_i - W_o)$$ $W_i$ and $W_o$ are the humidity ratios, which we can find on our chart:
![Psychrometric chart annotated with two points: (1) indoor air at ~12 g/kg and (2) outdoor air at ~4 g/kg humidity ratio](/assets/images/battling-mold-psychrometric-chart-annotated.png)
To revise, the humidity ratio tells us how much water we have per kg of dry air. We'll be moving ~12g of water out (1) and get ~4g of water in from outdoors (2). In total, a loss of roughly 8g per kg of dry air.
Thus, we can already qualitatively confirm that opening the windows does indeed help the fight with humidity.

What mass of dry air is in a $m^3$ of air? Yes, we can also determine that from the awesome chart. At (1) we have approximately $0.85 \frac{m^3}{kg_\text{dryair}}$.

Putting it all together:

> For each $m^3$ of air exchanged we dispose 0.0094 Liters of water.

#### Clearing the air

Good thing no one is mad. But since we learned that swapping indoor with outdoor air removes the loathed humidity from the mold-prone apartment, we are all for it.

An amazing German word needs to be part of this post. For one, because it precisely describes the most effective way to improve your air quality and reduce the humidity levels. For the other, it's fun.

> **Stosslüften**: Rapidly ventilate indoor spaces by opening all windows wide for a short period, typically around 5 to 10 minutes.

For Stosslüften, it is paramount to open as many windows as possible. To illustrate that importance: imagine only having one window open. The air needs to both enter and exit at the same time. This will slowly happen. But you will keep on exchanging already exchanged air since that's the one that's closest to the window. It is way more effective to have a flow, where fresh air comes in from one place and exits at another.

The apartment is $A = 54m^2$ and $h = 3m$ high. $150m^3$. We assume that we air properly (STOSSLÜFTEN!) and exchange 70% of all indoor air within 10 minutes. I have not gotten to install a CO2 Sensor at her place, but that would be an awesome proxy to determine whether most air has been exchanged. Maybe another time.

With that assumption, each STOSSLÜFTEN would make us lose
$$\|\Delta m_\text{water airing} \| = 150 [m^3] * 0.7 * 0.0094 [\frac{l}{m^3}] = 0.99 [l]$$
Is that a lot? Let's compare different water sources.

### Water Equilibrium

What water inputs do we have? I have large mental error bars for the estimates, but we have to start somewhere.
Going by the reasonably seeming LLM-Estimates:

- Human: 55g/h
- Human asleep: 40g/h
- 95% of the water you give to plants comes back into the air
- 30g/min shower (I would assume this to increase the hotter you shower)
- cooking (boiling water) 800 g/h
- 2500g per hand dried laundry

Water leaves the apartment through:

- Airing the room actively (Stosslüften)
- Passive air exit through the walls
- Potentially: The dehumidifier

$$\text{net water loss} = W_\text{out} - W_\text{in}$$

By now we are familiar with throwing some assumptions around:

- Water Creation per day
  - Humans: 55g/h \* 6h + 40g/h \* 9h = 0.7l
  - Plants Watering: 0.5l
  - Shower: 30g/min \* 10min = 0.3l
  - Cooking: 800g/h \* 0.25h = 0.2l
  - One hand dried laundry per 3 days: 0.8l
  - Total $W_\text{in}$: 2.5l
- Water exit:
  - Stosslüften 2 times per day: 1.98l
  - Passive air exit: $W_\text{passive}​=ACH * V_\text{apt}*24* (AH_{\text{in}}​−AH_\text{out}​)$
    - [ACH (Air Changes per Hour)](https://en.wikipedia.org/wiki/Air_changes_per_hour#Airtightness_in_building) 0.6 is the required standard for the "Passive House Standard". We assume 0.8 $[\frac{\text{Air Changes}}{h}]$. Though the standard test mimics the situation of sustained 32km/h wind. The "natural ACH" may be a factor of 10-25 times smaller. We go conservative and take $0.8/20 = 0.04$.
    - $\Delta$ AH Absolute Humidity: We check our psychrometric graph again and estimate a delta of 5g/m3
    - Total $W_\text{passive}​ = 0.04 * 150 [m^3] * 24 * 5 [\frac{g}{m^3}] = 0.72l$
  - Total $W_\text{out} = 2.7l$

Given the number of assumptions we made, 2.5l and 2.7l are pretty close. So on average, the assumptions say we air 
out enough water to compensate for the production. Why do we still have mold? 

Also, a better insulation decreases our ACH. Seemingly worsening the fight against mold. This goes against 
conventional wisdom. What are we missing?

### Why is the wall moist?

Our relative humidity indoors is measured at 70%. The air within the room is thus not moist, but the walls are battling mold. Why? The short answer is, that the wall temperature is lower than the room air temperature. Again, we want to reach a deeper understanding and be able to quantify things.

The walls are the insulation from the colder outdoor temperature $T_o$ to the cozy warmth indoor $T_i$. Across the wall, we have a temperature profile: on the outside it will be coldest and gradually get warmer towards the inside.

We'll be looking into three aspects:

- The temperature across the wall
- The heat exchange from inner and outer wall to the respective air

![Diagram of the temperature gradient across a wall, dropping linearly from warm indoor air through the wall to cold outdoor air, with convective steps at each surface](/assets/images/battling-mold-wall-temperature-gradient.png)

#### Temperature across the Wall

This section is a bit nerdy and not strictly necessary. If you don't like differential equations the graph above summarizes the findings. I think it's a neat example to show why engineering and maths are cool and hope it sparks some curiosity in some.

For those of you up to it, the [one-dimensional thermal conductivity equation](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node117.html) serves as basis to calculate how heat propagates through a material such as walls. We'll ignore that modern walls have (multiple) insulation layers and just assume it is a single material for now. This should not alter the high level understanding.

$$\rho c\frac{\delta T}{\delta t}=\frac{\delta}{\delta x}(\lambda\frac{\delta T}{\delta x})$$
$T$: Temperature($x$: position, $t$: time), $\rho$: density, $c$: specific heat capacity, $\lambda$: thermal conductivity

We can already draw conclusions from only looking into the steady-state description. Steady-state implies no changes over time, thus $\frac{\delta T}{\delta t}=0$. The equation above gets significantly easier:
$$0 =\frac{\delta^2T}{\delta x^2}$$

Integrating this twice, we see that the temperature drops linearly across the wall material in the steady state.
$$T(x) = C_1x+C_2$$
The two constants $C$ can be derived from boundary conditions such as the measured temperature at the inner wall. If your wall temperature is 18 degrees you'd set $T(x=0) = C_1*0+C_2 = 18$.

#### Heat Exchange with the Wall

This wall temperature is different than the air temperature. What factors affect how much heat is transferred from the air to the wall? [Convection](https://www.engineeringtoolbox.com/convective-heat-transfer-d_430.html) is the term used in thermodynamics to describe it:
The energy $q$ transferred through the area $A [m^2]$ intuitively depends on the temperature difference from wall and air $\Delta T$.
$$q = h_cA\Delta T [\frac{W}{m^2}]$$
$h_c$ is the coefficient that captures how efficiently heat flows between the two media. Here, we are interested in convection from air.
We differentiate between free and forced convection. Forced simply means, that there is an active airflow that speeds up the heat exchange. You might accurately guess, that this factor is hard to get right.
For this piece, we assume based on a [short internet search](https://en.wikipedia.org/wiki/Heat_transfer_coefficient#Overall_heat_transfer_coefficient):

- $h_c, \text{indoor} = 10 [\frac{W}{m^2K}]$, free convection
- $h_c, \text{outdoor} = 30 [\frac{W}{m^2K}]$, slightly forced convection due to a light wind

### Thermal Resistance

Analogous to electrical circuits, we can model our thermal system as an RC-Circuit with the following parallels:

- Heat Flux $Q$ <-> Current $I$
- Temperature $T$ <-> Voltage $V$
- Thermal Resistance $R_{th}$ <-> Resistance $R$

The thermal system of the house can thus be approximated by:
$$Q = \frac{T_\text{indoor} - T_\text{outdoor}}{R_\text{total}}$$
The three thermal resistors are in series
$$R_\text{total} = R_\text{conv,in} + R_\text{wall} + R_\text{conv,out} = \frac{1}{h_{c,in}A} + \frac{L}{\lambda A} + \frac{1}{h_{c,out}A}$$

> [!TIP]
> The RC-circuit analogy also allows the usage of the Voltage Divider Rule to find the wall surface temperature without calculating the actual heat flux $Q$
> $$T_\text{wall,surface,in} = T_\text{indoor} - (T_\text{indoor} - T_\text{outdoor}) \times \frac{R_\text{conv,in}}{R_\text{total}}$$

Let's put this to a test on my girlfriend's apartment. I sadly have no idea what elements her wall contains. Not overthinking this, let's just assume it is all concrete and use its [material properties](https://en.wikipedia.org/wiki/List_of_thermal_conductivities). In the fashion of Swiss houses built in that period, the wall is thick.
$$R_\text{total}\times A = \frac{1}{10[\frac{W}{m^2K}]} + \frac{0.8[m]}{1.5 [\frac{W}{mK}]} + \frac{1}{30[\frac{W}{m^2K}]} = \frac{2}{3} [\frac{m^2K}{W}]$$
$$T_\text{wall,surface,in} = 22 - (22 - 3) \times \frac{0.1}{\frac{2}{3}} = 19.2$$
Does this match reality?

### Verifying the assumption

Life passed and I didn't get to measure the wall temperature during winter. I don't own an infrared thermometer. Taping thermal probes to a wall would also be a good solution, but I was again not committed enough to prepare for it.

## Putting it all together

Recapturing, we have seen how psychrometrics work and realised the importance of the water mass equilibrium.
In the next chapter we covered how the temperature within walls can be drastically lower. Equipped with our psychrometrics knowledge, we understand the significance of it.

I wanted to put all those parameters into a model and with that evaluate the efficacy of preventive measures such as airing and the dehumidifier.

But well, other things popped up and this remained in this state for months. Publishing it now and might pick it up again later.

With it being summer now, it is interesting to evaluate whether it makes sense to keep the dehumidifier running.

## Dehumidifier in Summer

The mold problem is largely due to the lower capacity for water in colder air. E.g. the warm indoor air cools down in the walls, capacity is reached and droplets form.
This thermal difference from indoor to outdoor is significantly lower than in winter. With that, both indoor and outdoor have a similar capacity to carry water.

After multiple hot days, the walls might reach around 30 degrees. Reheating the indoor air, even during a cool night.

![Psychrometric chart showing summer conditions: 50% relative humidity at 30°C would only approach saturation if night temperatures drop below ~17°C](/assets/images/battling-mold-summer.png)

If we take a 50% relative humidity at 30 degrees, the night would need to be under 17 degrees to be in the realm of saturation possibility. In reality we still have the wall insulation dampening the problem. The outer wall will not be at outdoor temperature as it still carries a thermal mass.
Overall, my impression is that mold is no problem during summer. Which is reinforced by not knowing anyone having mold problems during summer.

## Questions for when I pick this topic up again

- Is it worthwhile bumping up the room temperature?
- How much water do I need to pump out of the air to stop the mold problem?
- The discussed model took steady state for everything, which does not match reality. Walls have a large thermal mass. With mold problems, water gets "stored" in walls and it needs to be pumped out over multiple days. Outdoor temperatures vary over multiple days.
