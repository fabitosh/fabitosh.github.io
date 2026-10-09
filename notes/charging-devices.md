---
description: "From the wall socket to the battery: plugs, chargers, cables, wireless standards, and how to charge without wearing out the battery."
btime: 2026-10-09
layout: note.njk
mtime: null
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
  - electronics
title: Charging Phones and Devices
---

I am contemplating a wireless charging dock for my phone and earbuds. The idea: whenever I'm home, the phone goes onto the dock. No cable fiddling, always topped up.
Before buying one, I wanted to understand what actually happens between the wall socket and the battery, and whether parking a phone on a charger all day hurts it.

<figure>
<svg viewBox="0 0 400 420" role="img" aria-label="Charging chain: wall socket to charger, then either a cable or a wireless pad, then the device" style="display:block; width:100%; max-width:440px; margin:0 auto; font-family:inherit">
<defs><marker id="charging-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker></defs>
<g fill="none" stroke="currentColor" stroke-width="1.5">
<rect x="100" y="10" width="200" height="56" rx="8"/>
<rect x="100" y="104" width="200" height="56" rx="8"/>
<rect x="14" y="216" width="176" height="62" rx="8"/>
<rect x="210" y="216" width="176" height="62" rx="8"/>
<rect x="100" y="344" width="200" height="62" rx="8" style="stroke: var(--pico-primary, currentColor)"/>
<path d="M298 278 V306 H200"/>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#charging-arrow)">
<path d="M200 66 V102"/>
<path d="M200 160 V188 H102 V214"/>
<path d="M200 188 H298 V214"/>
<path d="M102 278 V306 H200 V342"/>
</g>
<g fill="currentColor" text-anchor="middle" font-size="15">
<text x="200" y="34" font-weight="bold">Wall socket</text>
<text x="200" y="54" font-size="12">230 V AC, up to 2300 W</text>
<text x="200" y="128" font-weight="bold">Charger</text>
<text x="200" y="148" font-size="12">AC → DC, offers voltages</text>
<text x="102" y="241" font-weight="bold">Cable</text>
<text x="102" y="262" font-size="12">USB-C · PD / PPS / AVS</text>
<text x="298" y="241" font-weight="bold">Wireless pad</text>
<text x="298" y="262" font-size="12">Qi · Qi2 · MagSafe</text>
<text x="200" y="370" font-weight="bold">Device</text>
<text x="200" y="390" font-size="12">decides what it takes</text>
</g>
<g fill="currentColor" font-size="11" opacity="0.7">
<text x="208" y="89">AC</text>
<text x="208" y="180">DC, 5–48 V</text>
</g>
</svg>
<figcaption>The charging chain, from the wall socket to the battery.</figcaption>
</figure>

Following the chain, we'll cover:

1. **Wall to charger**: How much power the socket offers and whether a charger needs a grounding pin.
2. **Wired**: Connectors, cables and the protocols that negotiate how much power flows.
3. **Wireless**: Qi, Qi2, MagSafe and what the convenience costs.
4. **Chargers**: How multi-port chargers split power and what makes a good one.
5. **The battery**: What wears it down and how to charge without noticeable sacrifice.

## Wall to Charger

A Swiss household socket (type T13) delivers 230 V AC at up to 10 A:

$$
P = U \cdot I = 230\,\text{V} \cdot 10\,\text{A} = 2300\,\text{W}
$$

A phone charger draws 20–45 W, a laptop charger 65–140 W. The wall is never the bottleneck. It only becomes one when the charger shares a power strip with a kettle.

### Does a Charger Need a Grounding Pin?

Most phone chargers are double insulated (protection class II, the ⧈ symbol on the housing). Even if something fails inside, there is no live part you could touch. They don't need a ground for safety.

The grounding pin still helps in some cases:

- **Metal housings**: Switch-mode power supplies leak a tiny current through a filter capacitor (the Y-capacitor) that bridges their mains and low-voltage sides. On an ungrounded charger, you can feel it as a faint tingle on an aluminium laptop. A ground path drains it. That's why Apple's MacBook extension cable has a grounding pin.
- **Touchscreens**: The same electrical noise can make a touchscreen jumpy while charging, mostly with cheap chargers. Grounding can help.

It comes at a cost:

- **International use**: Grounded plugs are country-specific. Swiss T12, German Schuko and British type G don't fit each other's sockets. The ungrounded two-pin Europlug fits sockets across continental Europe, Switzerland included.
- **Size**: Three pins don't fold away as neatly.

For phones and earbuds, a Europlug charger is the better pick. For a stationary laptop or desktop charger, grounding is nice to have.

## Wired

Three parts decide how fast power flows: the connector, the cable and the protocol that charger and device agree on.

### Connectors

On the charger side, you find USB-A or USB-C. On the device side, almost everything new is USB-C.

| Connector | Shape (roughly to scale) | Where you find it | Charging |
|---|---|---|---|
| USB-C | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="USB-C outline"><rect x="7.6" y="8.9" width="24.8" height="7.2" rx="3.6" fill="none" stroke="currentColor" stroke-width="1.2"/><rect x="11" y="11.6" width="18" height="1.8" rx="0.9" fill="currentColor" opacity="0.35"/></svg> | Everything new. Mandatory in the EU for phones, earbuds and co. since end of 2024, for laptops since April 2026 | Up to 240 W. Reversible |
| USB-A | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="USB-A outline"><rect x="2" y="5.75" width="36" height="13.5" rx="0.6" fill="none" stroke="currentColor" stroke-width="1.2"/><rect x="4.5" y="8" width="31" height="4.5" fill="currentColor" opacity="0.35"/></svg> | Older chargers, computers, car sockets | No USB PD. Older or proprietary schemes (e.g. Quick Charge) reach about 18 W |
| Micro-USB | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Micro-USB outline"><path d="M9.7 9.8 H30.3 V12.6 L27.6 15.2 H12.4 L9.7 12.6 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Older Android phones, cheap gadgets | Mostly 5–10 W |
| Micro-USB 3.0 | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Micro-USB 3.0 outline"><path d="M1.6 9.8 H22.2 V12.6 L19.5 15.2 H4.3 L1.6 12.6 Z" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M23.4 9.8 H38.4 V12.6 L35.7 15.2 H23.4 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Older external hard drives, Galaxy S5 | 5 V. Mostly for data, enough to power a drive |
| Mini-USB | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Mini-USB outline"><path d="M9.8 8 H30.2 V11.5 L27.5 17 H12.5 L9.8 11.5 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Old GoPros, card readers, MP3 players, PS3 controllers | 5 V, slow |
| Lightning | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Lightning outline"><rect x="8.45" y="10.25" width="23.1" height="4.5" rx="2.25" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | iPhone 5 to 14, older AirPods | Up to ~27 W via USB PD with a USB-C to Lightning cable |
| USB-B | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="USB-B outline"><path d="M7.3 24.15 V5.5 L12 0.85 H28 L32.7 5.5 V24.15 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Printers, some audio and lab gear | Not relevant for charging |

### Cables

Any USB-C to USB-C cable up to 2 m carries 60 W (3 A at 20 V). That covers every phone. Only laptops above 60 W need a 5 A cable with an e-marker, a small chip that tells the charger it can handle the current ([up to 240 W](https://plugable.com/blogs/news/what-is-240w-usb-extended-power-range-epr)). The wattage logo on the packaging tells you which one you have. Data speed doesn't matter for charging.

### Protocols: Who Decides How Much Power Flows?

The charger never pushes power. It advertises what it can offer, and the device picks what it wants. Without an agreement, everything falls back to a safe 5 V. That's why a 140 W laptop charger is perfectly fine for earbuds.

| Protocol | Voltage | Max power | Notes |
|---|---|---|---|
| USB default | 5 V | 2.5–4.5 W | USB 2.0 / 3.x port on a computer |
| USB BC 1.2 | 5 V | 7.5 W | The classic "dumb" wall charger |
| USB-C Current | 5 V | 15 W | USB-C without negotiation, signalled via resistors |
| USB PD | 5 / 9 / 15 / 20 V | 100 W | The universal standard. What most devices use today |
| USB PD PPS | 3.3–21 V in 20 mV steps | 100 W | Required for Samsung's "Super Fast Charging" |
| USB PD AVS | 9–20 V (or 15–48 V) in 100 mV steps | 100 W (240 W) | PD 3.2. The iPhone 17 uses it |
| USB PD EPR | 28 / 36 / 48 V | 240 W | Laptops. Needs a 5 A e-marked cable |
| Proprietary | various | 100 W and more | Quick Charge, SuperVOOC, HyperCharge, ... Only with the brand's own charger and cable, falls back to PD otherwise |

Why bother with adjustable voltages (PPS, AVS)? A phone battery sits at around 3.5–4.4 V. With a fixed 9 V, the phone has to convert down itself, and the conversion losses turn into heat inside the phone, right next to the battery. With adjustable voltages, the phone asks the charger for exactly what it needs ("direct charging"). The conversion heat stays in the charger.

In practice, the differences are small. [Apple's 40 W adapter uses AVS](https://www.chargerlab.com/apple-iphone-17-series-debuts-with-40w-dynamic-power-adapter-and-pd-3-2-avs-fast-charging/) to charge the iPhone 17 to 50% in 20 minutes. [In PhoneArena's test](https://www.phonearena.com/news/iphone-17-fast-charge-speed-test_id174304), regular 45–65 W PD chargers still delivered about 36 W.

## Wireless

Wireless charging uses two coils. The charger's coil creates an alternating magnetic field, and the phone's coil turns it back into current. The further apart and the worse aligned the coils, the more energy is lost as heat. Magnets solve the alignment.

| Standard | Max power | Magnets | Notes |
|---|---|---|---|
| Qi | 5–15 W | No | The original. Position matters. iPhones were capped at 7.5 W |
| MagSafe | 15 W, 25 W from iPhone 16 | Yes | Apple's own, since iPhone 12 |
| Qi2 | 15 W | Yes | Open standard based on MagSafe's magnetic alignment. Recent iPhones, Pixel 10 |
| Qi2 25 W | 25 W | Yes | Since 2025. iPhone 16 and 17, Pixel 10 Pro XL |
| Qi2 Ready | 15–25 W | In the case | Phone speaks Qi2 but has no magnets. Needs a magnetic case. E.g. Samsung Galaxy S25/S26 |
| Proprietary | up to 50 W and more | Mostly no | Samsung, OnePlus, Xiaomi, ... Only with their own docks |

On Android, built-in magnets are still rare. [Belkin's compatibility chart](https://www.belkin.com/company/blog/qi2-compatible-devices/) keeps track of which phone does what.

### Efficiency: What Does the Convenience Cost?

Wired charging gets roughly 80–90% of the energy from the wall into the battery. Wireless is more like 60–75%, and worse when the coils are misaligned. Assuming 15 Wh into the battery per day (about one full charge of a large phone) at 0.30 CHF/kWh:

$$
\frac{15\,\text{Wh}}{0.65} - \frac{15\,\text{Wh}}{0.85} \approx 5.4\,\text{Wh per day}
$$

Over a year, that's about 2 kWh, or CHF 0.60. Add the dock's idle draw, which is worth measuring with a plug meter. At 0.5 W, it adds another 4.4 kWh, about CHF 1.30 per year.

Money is not the issue. The lost energy turns into heat, partly right next to the battery. That's the real cost.

## Chargers

### Multiple Ports

A multi-port charger has one power budget that's split across its ports. A 65 W charger with three ports might deliver 65 W on a single USB-C port, but only 45 + 20 W with two devices. The split is usually documented in a table on the product page. Check it for the combination you'd actually use.

When you plug in another device, many chargers briefly cut power to all ports to renegotiate. Phones don't care. A speaker or a small server might restart.

Multi-device wireless docks (phone, earbuds, watch) are multi-port chargers too. One power adapter feeds all pads. With a too weak adapter, the dock quietly drops the phone pad to a slower speed.

### What to Look Out For

- **USB-C with USB PD**: Plus PPS for Samsung phones. AVS gets the last few watts out of the newest iPhones.
- **Enough watts**: Add up what you charge at once and check the per-port split.
- **GaN** (gallium nitride): Smaller and cooler than a silicon charger of the same power. Almost standard by now.
- **Plug**: Europlug with foldable pins for travel. Grounded only for stationary laptop chargers.
- **Brand**: CE is a self-declaration. Cheap no-name chargers skimp on protection circuits and filtering (see the touchscreen jitter above). Stick to reputable brands.
- **Wireless**: Look for the official Qi2 logo. "Magnetic" or "MagSafe compatible" can mean plain Qi at 7.5 W with a magnet glued on. Check which power adapter the dock needs for full speed, often 30–45 W. Some 25 W docks have a fan, which is annoying in a bedroom.

## The Battery

> [!NOTE]
> Good news first: modern phones already handle most of what follows. They charge fast only when the battery is low, slow down when it fills up or gets warm, and offer settings to stop below 100%. The remaining job is not working against them.

### A First-Order Model

A lithium-ion battery shuttles lithium ions between two electrodes. Charging pushes them into the graphite anode, discharging lets them flow back into the metal-oxide cathode. Capacity is lost whenever lithium or electrode material drops out of that shuttle service for good.

### What Wears It Down

**Heat.** Unwanted side reactions speed up with temperature. They grow a crust on the anode (the solid electrolyte interphase, SEI) that permanently traps lithium. As a rule of thumb, reaction rates roughly double per 10 °C. [Apple names 16–22 °C](https://www.apple.com/batteries/maximizing-performance/) as the comfort zone.

**High charge level.** A full battery sits at its highest voltage. Both electrodes are at their extremes and the electrolyte decomposes more easily. That ages a battery even when it's lying in a drawer. Combined with heat, it gets bad. [Battery University](https://batteryuniversity.com/article/bu-808-how-to-prolong-lithium-based-batteries) estimates the remaining capacity after a year of storage:

| Temperature | Stored at 40% | Stored at 100% |
|---|---|---|
| 0 °C | 98% | 94% |
| 25 °C | 96% | 80% |
| 40 °C | 85% | 65% |
| 60 °C | 75% | 60% (after 3 months) |

**Mechanical stress.** Graphite swells by about 10% when it's packed with lithium and shrinks again when it empties. Every cycle is a breath. Over time, particles crack, and the protective SEI breaks open and regrows, consuming lithium each time. Deeper cycles mean bigger breaths. According to Battery University, a typical cell lasts about 300 full cycles (100% to 0%) before it drops to 70% capacity, but about 1000 cycles of 40%. Counted in delivered energy, that's 300 versus 400 full charges' worth. Shallow cycles help, but less than the raw numbers suggest.

Swollen batteries ("spicy pillows") are a different story. That's gas from decomposing electrolyte, mostly caused by heat and high voltage over a long time. The classic case: a laptop sitting at 100% on its charger for years.

**Fast charging when full or cold.** Ions need time to slot into the graphite. Push them faster than the graphite can take them, and they deposit as metallic lithium on its surface ("lithium plating"). That lithium is lost for good. The risk grows when the anode is already full (high charge level) and when it's cold (slow chemistry). Fast charging an empty battery at room temperature is much less of a problem.

**Running to 0%.** Hurts as well, but phones keep a hidden reserve and shut down before the cell is truly empty.

### What the Phone Already Does

Phones charge in two phases:

1. **Constant current**: Full speed while the battery is low. The voltage rises.
2. **Constant voltage**: Once the cell reaches its maximum voltage (somewhere around 60–80%), the phone holds the voltage and the current tapers off.

That's why fast charging is advertised as "50% in 20 minutes", and the last 20% take disproportionately long.

On top of that:

- Phones throttle or pause charging when they get hot. The iPhone shows "Charging on Hold".
- Optimized Charging (iOS) or Adaptive Charging (Android) learns your routine, holds at 80% overnight and finishes just before you usually unplug.
- Charge limits: iPhone 15 and later can stop anywhere between 80% and 100% in 5% steps. Pixel and Samsung phones offer an 80% limit, too.

## Practical Implications

What's at stake: A modern iPhone is rated to keep 80% of its capacity after 1000 full cycles. Charging once a day, that's almost three years. A battery replacement costs roughly a hundred francs. The goal is not to squeeze out every percent, but to avoid the few things that hurt a lot.

### Charging to 80%

In theory, it's a big lever. Battery University on the charge voltage of classic cells:

| Charge voltage | Cycles | Usable capacity |
|---|---|---|
| 4.20 V (full) | 300–500 | 100% |
| 4.06 V | 600–1000 | ~81% |
| 3.92 V | 1200–2000 | ~65% |

Modern phone cells charge to higher voltages and are built differently, so the absolute numbers don't transfer. The trend does.

In practice, the effect looks smaller. [MacRumors ran the 80% limit on three iPhones](https://www.macrumors.com/2026/10/06/iphone-17-pro-charge-limit/): The iPhone 15 Pro Max is at 88% after three years (369 cycles), the 17 Pro Max at 97% after one year (277 cycles). Readers without a limit report similar numbers. [BGR concluded](https://www.bgr.com/1979063/iphone-limit-charging-capacity-not-practical/) the limit made no meaningful difference after a year. These are anecdotes, not controlled tests. Still, the phone's own charge management seems to capture most of the benefit.

My take: Optimized Charging by default. An 80% limit if a day fits into 80%, lifted before a hike or a travel day.

### Fast Charging

Not a problem in itself. The phone decides the current and only charges fast when the battery is low and not too hot. With PPS or AVS, the conversion heat even stays in the charger. Slow overnight charging is slightly gentler, but there's no reason to avoid fast chargers.

What to avoid: charging while gaming, or while navigating in a hot car. Charging below freezing is bad too, but most phones refuse anyway.

### Wireless Charging With a Case

- Thin plastic or silicone cases of a few millimetres work fine.
- For Qi2 and MagSafe, the case needs a magnet ring. Otherwise, the phone doesn't snap into place, sits misaligned, and charges slower and hotter.
- Thick, rugged or leather cases insulate. Apple itself warns that charging inside certain cases can generate excess heat and recommends taking the phone out if it gets hot.
- Nothing metallic between phone and pad: cards in wallet cases, ring holders, metal plates for car mounts.

### Rules of Thumb

1. Avoid heat: no charging in direct sun, on the car dashboard, under the pillow or while gaming.
2. Let the phone manage: enable Optimized Charging or an 80% limit.
3. Don't leave it at 0% or 100% for long. For storage, aim for about 50%.
4. Top up whenever. Lithium-ion batteries have no memory effect. That was NiCd.

## So, the Dock?

Parking the phone on a dock for hours means a slightly warm phone at a high charge level. Exactly the combination to avoid. With the right setup, it's fine:

- **Qi2 certified, with magnets**: Aligned coils waste less energy as heat. Qi2 25 W if the phone supports it.
- **80% limit**: Optimized Charging is trained on overnight routines. A phone parked on a dock during the day may well sit at 100%. A fixed limit keeps it hovering between 75% and 80%.
- **A cool spot**: Not on the window sill.
- **A cable nearby**: Wired is faster and cooler for a quick top-up before leaving.

The earbuds have tiny batteries and draw little power. No concern there. The energy cost is negligible, as calculated above.

Verdict: Convenience wins, as long as heat stays in check.
