# Consistency Review: Wandyr v11.16

## Critical Mechanics Contradictions

### 1. Starting Hearts (Muster)
- **Location**: Line 106 vs Line 196
- **Issue**: 
    - Line 106 (Starting a Game) says: "Roll **1d6** Hearts for each of your three characters".
    - Line 196 (The Muster) says: "Roll **2d6** Hearts for each of your three characters".
- **Recommendation**: Standardize on one value. Given that weak monsters have d6 Hearts (Line 721), **2d6** seems more appropriate for heroes to survive.

### 2. Definition of "Spicy"
- **Location**: Line 310 vs Line 753 vs Line 755
- **Issue**:
    - Line 310 defines "Spicy" as **any die rolling a 1**, with double 1s being a "real penalty".
    - Line 753 (Death) refers to "Spicy" as **(double 1s)**.
    - Line 755 (Death) refers to "partially Spicy" as **(any die shows 1)**.
- **Recommendation**: Adopt consistent terminology.
    - *Suggestion*: 
        - **Spicy**: Any result with a single 1.
        - **Double Spicy / Critical Fail**: Double 1s.
    - Update Line 753 to say "Double Spicy (double 1s)" or similar if that is the intent.

## Terminology & Spelling

### 1. Magic School Names
- **Issue**: Inconsistent spelling of the Shadow magic school.
    - **Umbrakalla**: Lines 176, 178, 180, 392.
    - **Umbrakala**: Line 364.
    - **Umbrakallo**: Line 590.
- **Recommendation**: Change all instances to **Umbrakalla** (most frequent usage).

### 2. Hit Dice (HD)
- **Location**: Line 721
- **Issue**: The term "HD" is used ("Hearts per HD", "HD+2 Turns") but is not defined in the text. The game primarily uses "Level" and "Hearts".
- **Recommendation**: Replace "HD" with "Level" or define it explicitly if it differs from Level.

### 3. "Hits" vs "Hearts" in Combat
- **Location**: Line 739
- **Issue**: "reduce hits to each other by 1 Heart".
    - "Hits" usually implies the success of an attack.
    - "Hearts" implies damage.
- **Recommendation**: Clarify if this means "reduce damage taken by 1 Heart" or "reduce the attack roll result". Given the context of armor reducing damage (Line 737), it likely means damage.
    - *Proposed phrasing*: "reduce damage to each other by 1 Heart".

## Formatting & Structure

### 1. Header Levels
- **Location**: Line 590
- **Issue**: "Umbrakallo" header uses `#####` (Level 5), while other schools use `####` (Level 4).
- **Recommendation**: Change Line 590 to `#### 5 Umbrakalla (Shadow Gates)`.

### 2. Anchor Syntax
- **Location**: Line 332
- **Issue**: `## Names (#names)` uses parentheses instead of the curly brace syntax used elsewhere (e.g., `{#starting-a-game}`).
- **Recommendation**: Change to `## Names {#names}`.

### 3. Monster Levels
- **Location**: Line 716-717
- **Issue**: Level 8 is missing from the list (jumps from 7 to 9).
- **Recommendation**: Add a Level 8 monster or adjust the list.

### 4. Table of Contents
- **Issue**: The TOC contains page numbers (e.g., "Welcome to Wåndyr! 2") which are not relevant in a Markdown/digital format and may be confusing.
- **Recommendation**: Remove page numbers from the TOC.

## Clarifications Needed

### 1. Party Hearts
- **Location**: Line 200, Line 802
- **Question**: "Party Hearts can be used in place of character Hearts."
- **Clarification**: Does this mean any character can take damage to Party Hearts instead of their own? Is it a shared pool? How do they recover?

### 2. Turn Clock
- **Location**: Line 320
- **Question**: "The Guide loudly tosses a die into the clock... When the bowl has six dice".
- **Clarification**: Does the die face matter when tossed in? Or just that it is a die? (Presumably just a counter, but "tosses a die" might imply rolling).

### 3. Insight Options
- **Location**: Line 782
- **Observation**: The list of Insight options (1-6) is split by the "The above content does NOT show..." message in my initial read, but I verified it exists.
- **Note**: Ensure the list 1-6 is contiguous and clearly formatted.
