# Personalized Cheating Death Traits

A process for generating character-specific d66 Trait tables when a character returns from death using the Cheating Death rules.

---

## PROCESS OVERVIEW

When a character cheats death, instead of rolling on the generic "Cheating Death Marks" table, generate a personalized d66 table that reflects:

- Their existing Traits and nature
- Their Assets and equipment
- Their Names/abilities
- The specific circumstances of their death/transformation
- Their backstory and experiences

---

## INPUT REQUIREMENTS

To generate a personalized table, gather:

1. **Character Identity**
   - Name/alias
   - Existing Traits (e.g., Baesark, Vitae, Dwarf, etc.)
   - Ancestry/culture

2. **Character Assets**
   - Notable equipment/items
   - Weapons, armor, tools
   - Unique possessions

3. **Character Abilities**
   - Names (special abilities)
   - Spells or powers
   - Skills or techniques

4. **Death/Transformation Context**
   - How they died (if known)
   - What they were doing when they died
   - Any curses, corruption, or transformations they experienced
   - How long they were dead/missing
   - Any significant events during their absence

5. **Campaign Context**
   - The world/system they're in
   - Tone and themes of the campaign
   - Any relevant lore or magic systems

---

## GENERATION STEPS

### Step 1: Create the Framework

- Set up a d66 table (36 entries total: 1.1 through 6.6)
- Include a header explaining when/how the character returns
- Add the tone key: results with **1** = Spicy (ominous, cursed, scarred), results with **6** = Sweet (mystical, blessed)

### Step 2: Identify Key Themes

List the core elements to weave through the table:

- **Existing Traits** - How death/corruption changes them
- **Assets** - How items become cursed, enhanced, or corrupted
- **Abilities** - How powers invert, intensify, or transform
- **Death Experience** - Memories, lessons, or corruption from the time dead
- **Transformation** - Physical, mental, or spiritual changes
- **Specific Circumstances** - The unique events that led to death/return

### Step 3: Generate Entries (d66 Format)

For each of the 36 entries, create a Trait that:

- **Ties to character elements** - References their Traits, Assets, Names, or history
- **Reflects transformation** - Shows how death changed them
- **Maintains tone** - Spicy (1s) are ominous/cursed, Sweet (6s) are mystical/blessed
- **Is narratively interesting** - Creates hooks for future play
- **Feels personal** - Couldn't apply to just any character

**Distribution Strategy:**

- **1.x row** - Most Spicy, corruption-focused, ominous
- **2.x-5.x rows** - Mixed, transformational, ambiguous
- **6.x row** - Most Sweet, potentially redemptive or powerful

**Entry Format:**

- Each entry is a single sentence or short paragraph
- Describes the Trait clearly
- Implies narrative consequences
- May hint at mechanical effects (keep subtle)

### Step 4: Add GM Notes

Include optional mechanical nudges that:

- Stay minimal (avoid permanent stat changes)
- Focus on narrative impact
- Provide small advantages/disadvantages
- Suggest how Traits interact with the world

---

## EXAMPLE: AORFREDER

**Character:** Aorfreder (Baesark, Vitae)
**Assets:** Skeinsuit armor, Dryad Trophy Skulls, Kriegsmesser
**Names:** Peace Aura, Animal Bond
**Death Context:** Stole cursed chalice from chaos altar, failed save, became servant of evil, missing for a month

**Key Themes Identified:**

- Chaos altar corruption
- Berserker rage transformation
- Vitae (life-force) curdling
- Peace Aura inversion
- Animal Bond twisting
- Chalice's ongoing influence
- Month in chaos realm
- Trophy skulls becoming sentient
- Weapon bloodlust

**Sample Entries:**

- **1.1** (Spicy) - Chaos chalice corruption: black blood, dark energy in veins
- **1.3** (Spicy) - Trophy skulls whisper condemnation
- **2.3** (Mixed) - Peace Aura inverted, enemies grow aggressive
- **3.6** (Sweet) - Chaos altar marks soul, undead/demons recognize as kin
- **6.6** (Sweet) - Death grants boon: ignore death once per campaign

---

## TONE GUIDE

### Spicy (Contains 1)

- Ominous, cursed, scarred
- Physical corruption
- Dark transformations
- Loss of control
- Dangerous power
- Unwanted consequences

### Sweet (Contains 6)

- Mystical, blessed, redemptive
- Unexpected gifts
- Strange boons
- Useful abilities
- Positive transformations
- Mysterious but helpful

### Mixed (1-5, excluding 1s and 6s)

- Ambiguous transformations
- Both curse and gift
- Neutral but interesting
- Narrative hooks
- Character-defining without being purely good or bad

---

## SLASH COMMAND SPECIFICATION

When implementing as a slash command, the process should:

1. **Prompt for character information:**
   - Name, Traits, Assets, Names/abilities
   - Death circumstances
   - Time missing/transformation details

2. **Generate the table:**
   - Create 36 personalized entries
   - Ensure variety across the table
   - Tie entries to character elements
   - Balance Spicy/Sweet distribution

3. **Output format:**
   - Markdown file with proper d66 table structure
   - Header with character name and context
   - Tone key explanation
   - All 36 entries formatted clearly
   - Optional GM notes section

4. **Quality checks:**
   - Each entry references character-specific elements
   - Entries feel personal, not generic
   - Tone matches the table position (1s = Spicy, 6s = Sweet)
   - Narrative hooks are present
   - Mechanical suggestions are minimal

---

## BEST PRACTICES

- **Be Specific:** "Your Dryad Trophy Skulls whisper" is better than "trophies whisper"
- **Show Transformation:** Death should change them, not just mark them
- **Create Hooks:** Every Trait should suggest future narrative possibilities
- **Balance Power:** Even Spicy results can grant power, but at a cost
- **Keep It Personal:** The table should feel like it only works for this character
- **Maintain Tone:** Follow the Spicy/Sweet distribution naturally
- **Avoid Generic:** Don't use generic death/undeath themes—tie to the character

---

## TEMPLATE STRUCTURE

```markdown
# [Character Name] - Cheating Death Trait Table

[Context paragraph explaining when/how they return and what this table represents]

**Tone Key:** Any result containing a 1 is Spicy (ominous, cursed, [theme-specific]). Any result containing a 6 is Sweet (mystical, blessed, [theme-specific]).

---

## [CHARACTER]'S CHEATING DEATH TRAITS (d66)

**1.1** [Entry]   **1.2** [Entry]   **1.3** [Entry]   **1.4** [Entry]   **1.5** [Entry]   **1.6** [Entry]

**2.1** [Entry]   **2.2** [Entry]   **2.3** [Entry]   **2.4** [Entry]   **2.5** [Entry]   **2.6** [Entry]

[Continue through 6.6...]

---

## GM NOTES

[Context about the character's transformation]

**Mechanical Nudges (Optional):**
- [Specific entry references with minimal mechanical suggestions]
- [Keep mechanical effects minimal]

Keep the mechanical effects minimal—the real power is in how these Traits color the narrative and shape the character's interactions with the world.
```
