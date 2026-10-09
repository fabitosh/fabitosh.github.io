---
description: "Does a wireless charger on my desk damage my phone battery severely? The elements behind phone/gadget charging."
btime: 2026-10-09
layout: note.njk
mtime: null
permalink: notes/{{ page.fileSlug }}/index.html
status: draft
tags:
  - electronics
title: Wireless Charging without Guilt
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

A phone charger draws 20–45 W, a laptop charger 65–140 W. The wall is never the bottleneck with regular tech gear.

### Does a Charger Need a Grounding Pin?

Most phone chargers are double insulated (protection class II, the ⧈ symbol on the housing). Even if something fails inside, there is no live part you could touch. They don't need a ground for safety. The only benefit you might notice: on a metal laptop charging from a two-pin charger, some people feel a faint, harmless buzz when stroking the case. Many never do.

The grounding pin comes at a cost:

- **International use**: Grounded plugs are country-specific. Swiss T12, German Schuko and British type G don't fit each other's sockets. The ungrounded two-pin Europlug fits sockets across continental Europe, Switzerland included.
- **Size**: Three pins don't fold away as neatly.

For phones and earbuds, a Europlug charger is the better pick. For a charger that stays at home, three pins don't hurt.

## Wired

Three parts decide how fast power flows: the connector, the cable and the protocol that charger and device agree on.

### Connectors

On the charger side, you find USB-A or USB-C. On the device side, almost everything new is USB-C.

| Connector | Shape (roughly to scale) | Where you find it | Voltage | Max power |
|---|---|---|---|---|
| USB-C | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="USB-C outline"><rect x="7.6" y="8.9" width="24.8" height="7.2" rx="3.6" fill="none" stroke="currentColor" stroke-width="1.2"/><rect x="11" y="11.6" width="18" height="1.8" rx="0.9" fill="currentColor" opacity="0.35"/></svg> | Everything new. Reversible. Mandatory in the EU for phones, earbuds etc. since end of 2024, for laptops since April 2026 | 5–48 V | 240 W |
| USB-A | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="USB-A outline"><rect x="2" y="5.75" width="36" height="13.5" rx="0.6" fill="none" stroke="currentColor" stroke-width="1.2"/><rect x="4.5" y="8" width="31" height="4.5" fill="currentColor" opacity="0.35"/></svg> | Older chargers, computers, car sockets | 5–12 V | ~18 W |
| Micro-USB | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Micro-USB outline"><path d="M9.7 9.8 H30.3 V12.6 L27.6 15.2 H12.4 L9.7 12.6 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Older Android phones, cheap gadgets | 5–12 V | ~18 W |
| Micro-USB 3.0 | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Micro-USB 3.0 outline"><path d="M1.6 9.8 H22.2 V12.6 L19.5 15.2 H4.3 L1.6 12.6 Z" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M23.4 9.8 H38.4 V12.6 L35.7 15.2 H23.4 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Older external hard drives | 5 V | 4.5 W |
| Mini-USB | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Mini-USB outline"><path d="M9.8 8 H30.2 V11.5 L27.5 17 H12.5 L9.8 11.5 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Old GoPros, card readers, MP3 players, PS3 controllers | 5 V | ~5 W |
| Lightning | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="Lightning outline"><rect x="8.45" y="10.25" width="23.1" height="4.5" rx="2.25" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | iPhone 5 to 14, older AirPods | 5–9 V | 27 W |
| USB-B | <svg width="48" height="30" viewBox="0 0 40 25" role="img" aria-label="USB-B outline"><path d="M7.3 24.15 V5.5 L12 0.85 H28 L32.7 5.5 V24.15 Z" fill="none" stroke="currentColor" stroke-width="1.2"/></svg> | Printers, some audio and lab gear | 5 V | 4.5 W |

Anything above 5 V on the older connectors comes from fast-charging schemes on top, most commonly Qualcomm's Quick Charge on USB-A and Micro-USB, and USB PD through a USB-C to Lightning cable on Lightning.

### Cables

Any USB-C to USB-C cable up to 2 m is fine for charging up to 60 W. That covers every phone. Above 60 W, or if you also want fast data transfer, you need a cable rated for it. For power, that's a 5 A cable with an e-marker, a small chip that tells the charger it can handle the current ([up to 240 W](https://plugable.com/blogs/news/what-is-240w-usb-extended-power-range-epr)). The ratings are printed on the packaging.

### Protocols: Who Decides How Much Power Flows?

The charger never pushes power. It advertises what it can offer, and the device picks what it wants. Without an agreement, everything stays at a safe 5 V. That's why a 140 W laptop charger is perfectly fine for earbuds.

**USB Power Delivery (PD)** turns that agreement into a short digital conversation over a dedicated wire in the USB-C cable. The charger lists its offers, for example:

- 5 V at 3 A
- 9 V at 3 A
- 15 V at 3 A
- 20 V at 2.25 A

The phone requests one, the charger confirms and switches its output. That's the contract.

PD itself does not follow the battery. Once agreed, the charger holds its voltage, say 9 V. The battery sits somewhere between 3.5 and 4.4 V, depending on its charge level. A converter inside the phone steps the 9 V down and controls the current. As the battery fills, the phone draws less current, but the voltage stays where it is. The phone can renegotiate, but only between the fixed steps.

**PPS and AVS** add adjustable voltages to PD. Instead of picking one of the fixed steps, the phone requests an exact voltage (in 20 mV steps for PPS, 100 mV for AVS) and re-requests every few seconds as the battery voltage rises. The charger effectively becomes the phone's charging circuit. Inside the phone, a simple and very efficient stage halves the voltage and doubles the current (a charge pump). It can't regulate anything itself: its output is always half its input. So as the battery voltage climbs from about 3.7 to 4.4 V, the phone asks for a little more voltage to keep the current flowing.

> [!NOTE]
> Why exactly half? A charge pump is little more than a capacitor and a few switches, flipping between two positions hundreds of thousands of times per second. In the first, the capacitor sits between input and output, so it charges up to the difference between the two. In the second, it sits next to the battery and discharges into it, so it ends up at the battery's voltage. Both only hold if input minus output equals output, which makes the output exactly half the input. And every bit of charge taken from the charger reaches the battery twice, once in each position, so the current doubles.

Here's what that looks like for a phone at 10%, charging at about 18.5 W (rough numbers):

| | Fixed PD | PD PPS |
|---|---|---|
| Phone requests | 9 V | 7.6 V |
| Charger delivers | 9 V × 2.2 A ≈ 20 W | 7.6 V × 2.5 A ≈ 19 W |
| Conversion in the phone | Step-down converter, ~92% | Charge pump, ~97% |
| Into the battery | 3.7 V × 5 A ≈ 18.5 W | 3.7 V × 5 A ≈ 18.5 W |
| Heat in the phone | ~1.6 W | ~0.5 W |
| As the battery fills | Voltage stays at 9 V, current drops | Voltage creeps up with the battery to about 9 V, then current drops |

AVS follows the same idea: the voltage rises with the battery, in 100 mV steps from 9 V upward. That floor is too high for the simple halving above, so the phone needs a different conversion stage. Apple doesn't publish how the iPhone 17 does it.

How helpful are those voltage steps over regular USB PD? At typical phone wattages, barely. [Apple's 40 W adapter uses AVS](https://www.chargerlab.com/apple-iphone-17-series-debuts-with-40w-dynamic-power-adapter-and-pd-3-2-avs-fast-charging/) to charge the iPhone 17 to 50% in 20 minutes, but [in PhoneArena's test](https://www.phonearena.com/news/iphone-17-fast-charge-speed-test_id174304), regular 45–65 W PD chargers still delivered about 36 W. Their real job is making high-power charging possible: at 45 W, a 92% converter would leave almost 4 W of heat inside the phone, a charge pump about 1.5 W. Samsung builds its 25 and 45 W modes on PPS, so without it, a Galaxy falls back to 15 W.

For reference, the whole family:

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

Want to go deeper? Texas Instruments' [An Engineer's Guide to USB Type-C](https://www.ti.com/lit/eb/slyy228/slyy228.pdf) is an excellent e-book on USB-C and Power Delivery.

## Wireless

Wireless charging uses two coils. The charger's coil creates an alternating magnetic field, and the phone's coil turns it back into current.

**Alignment makes or breaks it.** The coils only couple well when they sit right on top of each other. A few millimetres off, and a growing share of the energy turns into heat instead of charge. The phone warms up and throttles, so a misaligned phone charges slower and hotter at the same time. With plain Qi, positioning is up to you. Magnets (MagSafe, Qi2) snap the coils into the same spot every time. That, more than the extra watts, is the reason to pick Qi2 over plain Qi.

| Standard | Max power | Magnets | Notes |
|---|---|---|---|
| Qi | 5–15 W | No | The original. Positioning is up to you. iPhones were capped at 7.5 W |
| MagSafe | 15 W, 25 W from iPhone 16 | Yes | Apple's own, since iPhone 12 |
| Qi2 | 15 W | Yes | Open standard based on MagSafe. iPhone 13 to 15, Pixel 10 and 10 Pro |
| Qi2 25 W | 25 W | Yes | Since 2025. iPhone 16 (not the 16e) and 17, Pixel 10 Pro XL |
| Qi2 Ready | 15–25 W | In the case | Phone speaks Qi2 but has no magnets. Needs a magnetic case. E.g. Samsung Galaxy S25 |
| Proprietary | up to 50 W and more | Mostly no | Samsung, OnePlus, Xiaomi, ... Only with their own docks |

On Android, built-in magnets are still rare. [Belkin's compatibility chart](https://www.belkin.com/company/blog/qi2-compatible-devices/) keeps track of which phone does what.

### Efficiency: What Does the Convenience Cost?

Wired charging gets roughly 80–90% of the energy from the wall into the battery. Wireless is more like 60–75% when well aligned, and drops quickly when it isn't. Assuming 15 Wh into the battery per day (about one full charge of a large phone):

$$
\frac{15\,\text{Wh}}{0.65} - \frac{15\,\text{Wh}}{0.85} \approx 5.4\,\text{Wh per day}
$$

Over a year, that's about 2 kWh. For perspective:

- A person in a Swiss flat without electric heating uses roughly 1,100 kWh of electricity per year. Wireless charging adds about 0.2%.
- An electric car uses 15–20 kWh per 100 km. A year of wireless losses takes it about 10 km. One full charge of a 60 kWh car battery covers 30 years of them.

Idle draw is a separate question, and it applies to wired chargers just as well. A charger left in the socket draws a little power even without a phone attached. EU rules cap that at 0.1 W for phone-sized power adapters, about 0.9 kWh per year. A well-designed dock idles in the same range, a cheap one might draw a few tenths of a watt. A plug meter tells.

In money, at 0.30 CHF/kWh: about CHF 0.60 per year for the wireless losses, and up to CHF 0.30 per idling charger.

Money and energy are not the issue. The lost energy turns into heat, partly right next to the battery. That's the part to keep an eye on, especially with a case.

## Chargers

### Multiple Ports

A charger's rating is the total across all its ports. A 65 W charger with three ports might deliver 65 W on a single USB-C port, but only 45 + 20 W with two devices. Who gets what is decided by the charger's power management: a small controller chip that runs the PD negotiation on each port and splits the shared budget. Its rules are documented in the datasheet or on the product page, usually as a table of port combinations. Check it for the combination you'd actually use.

When you plug in another device, many chargers briefly cut power to all ports to renegotiate. Phones don't care. A speaker or a small server might restart.

Multi-device wireless docks (phone, earbuds, watch) are multi-port chargers too. One power adapter feeds all pads. With a too weak adapter, the dock quietly drops the phone pad to a slower speed.

### What to Look Out For

- **USB-C with USB PD** as the baseline. PPS and AVS are optional extensions. A charger doesn't get them automatically by supporting PD, so they must be listed explicitly on the spec sheet ("PPS", "AVS", or an output range like "3.3–21 V"). Without them, phones fall back to fixed PD. That's fine for most phones, but Samsung needs PPS for anything above 15 W.
- **Enough watts**: The rating is the total. Add up what you charge at once and check the per-port table.
- **GaN** (gallium nitride): Smaller and cooler than a silicon charger of the same power. Almost standard by now.
- **Plug**: Two pins (Europlug) for travel. For a charger that stays at home, three pins don't hurt.
- **Brand**: CE is a self-declaration. Cheap no-name chargers skimp on protection circuits and filtering. Stick to brands with a good track record, e.g. Anker, Ugreen, Belkin, Satechi, Apple, Samsung or Google, and Nomad or ESR for docks. [ChargerLab](https://www.chargerlab.com/) tears chargers apart and shows what's inside.
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

**Mechanical stress of a charge cycle.** Graphite swells by about 10% when it's packed with lithium and shrinks again when it empties. Every charge cycle is a breath. Over time, particles crack, and the protective SEI breaks open and regrows, consuming lithium each time. Deeper cycles mean bigger breaths, so frequent small top-ups are gentler than running the battery down and charging it full. According to Battery University, a typical cell lasts about 300 full cycles (100% to 0%) before it drops to 70% capacity, but about 1000 cycles of 40%. Even counted in delivered energy (300 versus 400 full charges' worth), shallow cycles win.

Swollen batteries ("spicy pillows") are a different story. That's gas from decomposing electrolyte, mostly caused by heat and high voltage over a long time. The classic case: a laptop sitting at 100% on its charger for years. A swollen battery is broken. Stop charging it, don't press or puncture it, and have it replaced. It's a fire risk.

**Fast charging when full or cold.** Ions need time to slot into the graphite. Push them faster than the graphite can take them, and they deposit as metallic lithium on its surface ("lithium plating"). That lithium is lost for good. The risk grows when the anode is already full (high charge level) and when it's cold (slow chemistry). Fast charging an empty battery at room temperature is much less of a problem.

**Running low.** Less harmful than the top end. A high charge level stresses the battery for as long as it sits there. A low one mostly doesn't, because the 0% your phone shows is not truly empty: phones keep a hidden reserve. It only becomes harmful when a phone sits empty for weeks. Self-discharge can then pull the cell below its safe minimum and damage it for good. The gentlest range is the middle.

### What the Phone Already Does

Phones charge in two phases:

1. **Constant current**: Full speed while the battery is low. The voltage rises.
2. **Constant voltage**: Once the cell reaches its maximum voltage (somewhere around 60–80%), the phone holds the voltage and the current tapers off.

That's why fast charging is advertised as "50% in 20 minutes", and the last 20% take disproportionately long.

On top of that:

- Phones throttle or pause charging when they get hot. The iPhone shows "Charging on Hold".
- Optimized Charging (iOS) or Adaptive Charging (Android) learns your routine. When it expects a long charging session, like overnight, it holds at 80% and finishes just before you usually unplug.
- Charge limits: iPhone 15 and later can stop anywhere between 80% and 100% in 5% steps. Pixel and Samsung phones offer an 80% limit, too.

## Practical Implications

What's at stake: A modern iPhone is rated to keep 80% of its capacity after 1000 full cycles. Charging once a day, that's almost three years. A battery replacement costs roughly a hundred francs. The goal is not to squeeze out every percent, but to avoid the few things that hurt a lot.

### In Practice: Long-Term Tests

The chemistry above tells us what wears a battery down, but not by how much in everyday charging. HTX Studio built automated rigs that drain and recharge phones around the clock, and ran two long-term tests.

The [first](https://www.youtube.com/watch?v=kLS5Cg_yNdM) ran iPhone 12s and Android phones (iQOO 7, fast charging at 120 W) through 500 charge cycles. Per phone model, a few phones each were slow-charged or fast-charged between 5% and 100%, another group was fast-charged only between 30% and 80%, and one phone was never charged as a control. Capacity lost after 500 cycles:

| Group | iPhone 12 | iQOO 7 |
|---|---|---|
| Slow, 5–100% | 11.8% | 8.8% |
| Fast, 5–100% | 12.3% | 8.5% |
| Fast, 30–80% | 8.3% | 6.0% |

Fast versus slow made no meaningful difference, even at 120 W. Staying between 30% and 80% cut the wear by about 30% on both phones.

The [second](https://www.youtube.com/watch?v=Lj4LMlGr4og) compared wired and wireless charging on iPhones, all on Apple's 20 W adapter. One group comes close to the dock scenario: phones topped up between 80% and 95% on a wireless charger, over and over. Capacity lost after 2000 hours:

| Group | Capacity lost |
|---|---|
| Wired, 5–100% | 9.0% |
| Wireless, 5–100% | 9.0% |
| Wireless, 80–95% | 3.9% |

Wireless charging wore the batteries no more than a cable. And frequent top-ups on the pad didn't hurt: that group lost the least.

What the tests don't cover:

- **Sample size**: A handful of phones per group. HTX itself labels the results as for reference only.
- **Sitting full**: Both tests cycled the phones nonstop. Neither captures a phone simply sitting at 100% for days. That's calendar aging, and the storage table above suggests a limit matters even more there.
- **Cases**: The phones charged without one. A case adds distance between the coils and insulates the battery, so lower efficiency and more heat.

### Charging to 80%

In theory, it's a big lever. Battery University on the charge voltage of classic cells:

| Charge voltage | Cycles | Usable capacity |
|---|---|---|
| 4.20 V (full) | 300–500 | 100% |
| 4.06 V | 600–1000 | ~81% |
| 3.92 V | 1200–2000 | ~65% |

Modern phone cells charge to higher voltages and are built differently, so the absolute numbers don't transfer. The trend does. The first test above confirms the direction with a smaller effect: about 30% less wear for 30–80%.

### Fast Charging

Not a problem in itself, as the first test shows. The phone decides the current and only charges fast when the battery is low and not too hot. With PPS or AVS, the conversion heat even stays in the charger.

What to avoid is real heat: direct sun or a car dashboard in summer. Charging below freezing is bad too, but most phones refuse anyway.

### Wireless Charging With a Case

- Thin plastic or silicone cases of a few millimetres work fine. Every millimetre adds distance between the coils and costs a little efficiency.
- For Qi2 and MagSafe, the case needs a magnet ring. Otherwise, the phone doesn't snap into place, sits misaligned, and charges slower and hotter.
- The magnets only align. They don't strengthen or extend the charging field: they are static, while the charging field alternates rapidly.
- Thick, rugged or leather cases insulate. Apple itself warns that charging inside certain cases can generate excess heat and recommends taking the phone out if it gets hot.
- The phone doesn't know about the case, but it notices the result. It measures the battery temperature and throttles regardless of the cause. iPhones may pause at 80% when the battery runs warm.
- Nothing metallic between phone and pad: cards in wallet cases, ring holders, metal plates for car mounts. Most chargers detect foreign metal and stop.

### Rules of Thumb

1. Avoid real heat: no charging in direct sun, on the car dashboard or under the pillow.
2. Let the phone manage: enable Optimized Charging or an 80% limit.
3. Don't leave it at 0% or 100% for long. For storage, aim for about 50%.
4. Top up whenever. Lithium-ion batteries have no memory effect. That was NiCd.

## So, the Dock?

Ultimately, we can do almost anything for convenience, as long as we keep the battery cool.

Parking the phone on a dock for hours means a slightly warm phone at a high charge level. Exactly the combination to avoid. With the right setup, it's fine:

- **Qi2 certified, with magnets**: Aligned coils waste less energy as heat. Speed hardly matters when the phone sits there for hours, and slower runs cooler.
- **80% limit**: Optimized Charging only kicks in when the phone expects one long charging session, and it still aims for 100% by the time you unplug. A dock means many short sessions. A fixed limit is predictable: it keeps the phone between 75% and 80%.
- **A cool spot**: Not on the window sill.
- **A cable nearby**: Wired is faster and cooler for a quick top-up before leaving.

HTX's 80–95% wireless group shows that frequent top-ups, exactly what a dock does, are not bad for the battery. It's not an exact replica of my setup, though: those phones charged without a case. Mine has one, so a bit less efficiency and more heat. The earbuds have tiny batteries and draw little power. No concern there. The energy cost is negligible, as calculated above.

For me, this will be slow wireless charging capped at 80%, with an occasional fast charge to 100% by cable when I need it.
