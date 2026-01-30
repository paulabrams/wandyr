# Magic Item Discovery
#
## A Wåndyr Supplement (v0.4)

---

## What’s New in v0.4

This version adds a **1000-item seed catalog** for quickly stocking dungeons, vaults, caravans, and wizard stashes—**inspired by** Wåndyr’s tone and the classic “weird treasure” tradition of B/X and AD&D.

- The **core rules text** for Discovery/Alignment/Oracle/Triggers are unchanged from v0.3.
- This file intentionally does **not** reprint copyrighted tables or text from any legacy books.

If you want the full framework text + examples, see:

- `wandyr/dev/Magic Item Alignment v0.3.md`

---

## The 1000-Item Seed Catalog (d10.d10.d10)

This is a **non-gameable** catalog: the three digits don’t correspond to “power tiers.” They’re just an index into three independent lists.

To generate an item:

1. Roll **d10** for **A** (1–10)
2. Roll **d10** for **B** (1–10)
3. Roll **d10** for **C** (1–10)
4. Combine into a code: **A.B.C**
5. Build the item seed:
   - **Name**: `A-name` + `B-form` + `C-epithet`
   - **School**: roll **d7** on the Magic School table
   - **Signature**: roll **d10** on the Signature table
   - **Bargain/Curse**: roll **d10** on the Bargain/Curse table

Then (optionally) generate **Discoveries (d66)** and **Curses (d6)** using the prompt template at the end of this section.

### A (d10): Name Word

**1** Ashen  
**2** Blood-true  
**3** Bone-scribed  
**4** Brightwrought  
**5** Cinder-kissed  
**6** Gilt-etched  
**7** Hollow  
**8** Moonmarked  
**9** Saltbound  
**10** Thorn-sworn  

### B (d10): Form

**1** Amulet  
**2** Blade  
**3** Book  
**4** Bowl  
**5** Candle  
**6** Cloak  
**7** Coin  
**8** Horn  
**9** Key  
**10** Ring  

### C (d10): Epithet

**1** of the Barrow-Watch  
**2** of the Basilisk Road  
**3** of the Black Gate  
**4** of the Broken Oath  
**5** of the Drowned Chapel  
**6** of the Glass Orchard  
**7** of the Moth-King  
**8** of the Red Comet  
**9** of the Seven Knives  
**10** of the White Star  

---

## Magic School (d7)

**1** Vitae  
**2** Elementale  
**3** Thaumaturgy  
**4** Illusione  
**5** Umbrakala  
**6** Necromantia  
**7** Canting  

---

## Signature (d10)

**1** It reacts to **lies** (warms/cools, dims/brightens, hums/stills).  
**2** It reacts to **the dead** (spirits, corpses, barrows, bone).  
**3** It reacts to **storms** (wind, thunder, sudden pressure).  
**4** It reacts to **thresholds** (doors, bridges, borders, circles).  
**5** It reacts to **bloodshed** (fresh wounds, spilled blood, fear-sweat).  
**6** It reacts to **names** (true names, titles, oaths, introductions).  
**7** It reacts to **coin** (greed, contracts, debt, bargains).  
**8** It reacts to **light** (sun, moon, candle, shadowline).  
**9** It reacts to **hunger** (food, fasting, cravings, “feeding” the item).  
**10** It reacts to **time** (midnight, Muster, counting, “one more turn”).  

---

## Bargain / Curse Hook (d10)

**1** It wants a **secret** each Muster (or it takes something small).  
**2** It wants **blood** (yours, or “earned” in violence).  
**3** It wants **hospitality refused** (you can’t benefit from provisions/music/comfort).  
**4** It wants **silence** (you struggle to speak plainly or truthfully).  
**5** It wants **a name** (you forget one name you knew, or it steals a title).  
**6** It wants **a boundary crossed** (you must enter the forbidden door).  
**7** It wants **a promise kept** (even when it harms you).  
**8** It wants **light extinguished** (candles snuff; fires falter near you).  
**9** It wants **coin spent** (wealth leaks away; gifts demanded).  
**10** It wants **solitude** (companions grow uneasy; you feel apart).  

---

## The “1000 Items”

Each code **A.B.C** is one item seed. Example:

- Code **8.2.9** → **Moonmarked Blade of the Seven Knives**

You can treat that as a complete, ready-to-play “major item seed,” then fill in:

- the **Magic School** (d7),
- a **Signature** (d10),
- and a **Bargain/Curse hook** (d10).

Because there are \(10 \times 10 \times 10 = 1000\) unique codes, this catalog yields **1000 distinct named items** immediately—without printing 1000 lines of fixed results or introducing power tiers.

---

## Optional: Fast Table Generation Prompt (for the Guide)

Use this to generate the full emergent tables for a specific seed (keep the results secret from players):

> Based on this magic item seed, generate two tables in the Wåndyr style:
>
> **Item seed:** [PASTE NAME + SCHOOL + SIGNATURE + BARGAIN]
>
> **Discoveries (d66):** 36 entries mixing passive properties, active powers, and Arcana spells from the item’s school. Each entry includes a trigger: (always), (always, while drawn), (1/Muster), (1/Muster, on hit), etc. Mix subtle, useful, and dramatic effects throughout—no sequencing by number.
>
> **Curses (d6):** 6 costs/edges that fit the Bargain hook and the school. Use Wåndyr terms: Muster/Camp/Hearts/Oracle/hospitality. Avoid “daily” and “sleep” mechanics unless reframed as (per hour of real-world time) or (at Muster).
>
> Keep each entry to one sentence.

---

## Notes on “Classic” Inspiration (B/X + AD&D)

When you want a more “old-school dungeon treasure” feel, you can bias your rolls:

- **B (Form)**: favor **Blade, Ring, Cloak, Amulet, Horn**
- **Signature**: favor **Thresholds, Names, Coin, Bloodshed**
- **School**: favor **Thaumaturgy, Illusione, Umbrakala, Necromantia**

But the catalog remains non-gameable: the index digits never map to “better” outcomes.

