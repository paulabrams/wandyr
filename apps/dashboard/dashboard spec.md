# Wåndyr Session Dashboard Specification

Version: 1.4
Date: January 21, 2026

## Overview

A web-based session management tool for Wåndyr tabletop RPG. Designed for screen-sharing via Zoom while running games with remote players. Must be mobile-friendly for Guide use on tablets/phones.

---

## Data Model

### Session State

```json
{
  "session": {
    "round": 0,
    "turn": 0,
    "insight": 0
  },
  "adventure": {
    "target": null,
    "total": null,
    "result": ""
  },
  "environment": {
    "region": "Wåndyrwyld",
    "climate": "Temperate",
    "landform": "Deciduous forest",
    "terrain_condition": "",
    "poi": "",
    "conditions": "1.1 Clear & Mild"
  },
  "dice": {
    "rolls": [3, 4],
    "type": "normal", // normal, adv, dis
    "total": 7
  },
  "rumor": {
    "text": "",
    "blessing": {
      "active": false,
      "source": "",
      "value": 0
    }
  },
  "mode": "muster", // "camp" or "muster"
  "muster": [],
  "camp": [],
  "threats": []
}
```

### Character Object

```json
{
  "id": "uuid",
  "number": 1,
  "name": "Bjel",
  "description": "Thaumaturge relic-hunter",
  "notes": "Has the Staff of Athyr-Vok",
  "leader": false,
  "blessed": false,
  "baggage": false,
  "hearts": { "current": 7, "max": 7 },
  "iron": { "current": 0, "max": 4 },
  "arcana": { "current": 2, "max": 2 }
}
```

### Threat Object

```json
{
  "id": "uuid",
  "name": "Orc Chief",
  "description": "Scarred veteran with notched blade",
  "level": 2,
  "oracle": "10",
  "condition": "active"
}
```

---

## UI Layout

### Global Elements

- **Header**: Title "Wåndyr" + Actions Menu (Hamburger/Gear icon).
- **Actions Menu**:
  - Switch Mode (Camp / Muster)
  - Export JSON
  - Import JSON
  - Reset Session

### Modes

#### 1. Camp Mode

*Used for session setup, resting, and preparing the party.*

Layout:

- **Rumor & Blessing Card**:
  - Input: Current Rumor.
  - Input: Blessing Source (Name of Being).
  - Input: Blessing Value (Number of Hearts).
  - Toggle: Blessing Active (Apply/Remove).
- **Roster Management**:
  - Two lists: **The Muster** (Active) and **The Camp** (Inactive).
  - Drag-and-drop or "Move" buttons to swap characters between lists.
  - "Add Character" button.
  - Full edit capability for characters.

#### 2. Muster Mode (Play Mode)

*Used during gameplay.*

Layout:

- **Environment Card** (Separate from Header):
  - Values: Region, Terrain, Weather.
  - Weather Dice display.
- **The Muster**: Active characters only.
- **Threats**: Active threats.

### Responsive Breakpoints

- **Desktop** (≥1024px): Three-column layout in Muster Mode.
- **Tablet** (768px–1023px): Two-column layout.
- **Mobile** (<768px): Single-column stacked layout.

### Desktop Layout (Muster Mode)

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER: Title  [Wåndyr]                       [Actions (=)] │
├─────────────────────────────────────────────────────────────┤
├──────────────┬─────────────────────────┬────────────────────┤
│   LEFT COL   │      THE MUSTER         │       OTHERS       │
│              │                         │                    │
│ WHERE ARE WE │  [Character Cards]      │  [Other Cards]     │
│ (Location)   │                         │                    │
│              │                         │                    │
│  INSIGHT     │                         │                    │
│  [SKILL]     │                         │                    │
│              │                         │                    │
│  Turn: 0     │                         │  [+ Add Other]     │
│  Round: 0    │                         │                    │
│ [+Turn]      │                         │                    │
│ [+Round]     │                         │                    │
│ [Roll Insight]                          │                    │
│              │                         │                    │
│ ADVENTURE    │                         │                    │
│ [Easy] [Avg] [Hard]                    │                    │
│ Result...    │                         │                    │
│              │                         │                    │
│ ORACLE       │                         │                    │
│ ⚀ ⚁ ⚂ [Roll] │                         │                    │
└──────────────┴─────────────────────────┴────────────────────┘
```

### Desktop Layout (Camp Mode)

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER: Title  [Wåndyr]                       [Actions (=)] │
├─────────────────────────────────────────────────────────────┤
│ RUMOR & BLESSING                                            │
│ Rumor: [_______________________]                            │
│ Blessing: [___] Hearts from [___________]  (Active [x])     │
├──────────────────────────┬──────────────────────────────────┤
│        THE MUSTER        │            THE CAMP              │
│   (Who is going out)     │        (Who is staying)          │
│                          │                                  │
│   [Character Card]       │        [Character Card]          │
│   [Character Card]       │        [Character Card]          │
│                          │                                  │
│   [< Move to Camp]       │        [Move to Muster >]        │
│                          │                                  │
│   [+ Add Character]      │                                  │
└──────────────────────────┴──────────────────────────────────┘
```

---

## Components

### Environment Card (Muster Mode)

- **Region**: Text Input.
- **Climate Zone**: Dropdown (Polar, Boreal, Temperate, Subtropical, Tropical, Equatorial).
- **Landform**: Dropdown + Randomize Button (⟳). Dynamic options based on Zone (d6 table).
- **Transition**: Dropdown + Randomize Button (⟳) (d6 table).
- **Transition To**:
  - If **Transition is 1–3**: always **inherits the current Landform** (same landform).
  - If **Transition is 4–6**: auto-rolls a **different** landform (within the current Climate), but may be manually selected.
- **Condition**: Text Input + Random Button (⟳) (Tier 4).
- **Point of Interest**: Text Input + Random Button (⟳) (Tier 5).
- **Conditions (Weather)**: Dropdown + Randomize Button (⟳). Populated from `weather.md` (Standard) and `weather shifts.md` (Shifts).

### Oracle Dice Card (Muster Mode)

- **Heading**: "Oracle" is a standard card title on its own line (matches Adventure card styling).
- **Buttons**: **Roll**, **Adv**, **Dis**.
- **Layout**: Buttons on one row; **result displayed beneath the buttons** (matches Adventure card).
- **Display**:
  - Normal: 2 dice pips.
  - Adv/Dis: 3 dice pips (visually indicate dropped die).
  - **Total**: Sum of kept dice.

### Adventure Card (Muster Mode)

- **Purpose**: Quick “does trouble find you?” roll at the table.
- **Buttons**:
  - **Easy** (Target 6) — safe areas
  - **Average** (Target 8) — normal travel / uncertain spaces
  - **Hard** (Target 10) — dangerous areas
  - **Extreme** (Target 12) — monster lairs / extremely dangerous places
- **Roll**: 2d6 vs target.
  - If \(total \ge target\): “All clear”
  - Else: “Adventure!”
- **Display**: Shows last total, target, and result text.

### Rumor & Blessing (Camp Mode)

- **Rumor**: Text area.
- **Blessing**:
  - **Source**: Text Input (e.g., "The Forest Spirit").
  - **Value**: Number Input (e.g., 2).
  - **Active**: Checkbox/Toggle.
  - *Effect*: When active, characters marked as 'Blessed' receive a visual cue (Gold Glow). The 'Value' is for reference by the Guide (e.g., "You all have 2 extra Iron Hearts").

### 7. **Others (NPCs & Threats) (All Modes)**

- **Header**: "Others" (previously Threats).
- **List**: Display list of NPCs/monsters.
- **Reorder (Drag & Drop)**:
  - Other cards can be dragged to reorder the list.
  - Order persists (saved in session state).
- **Card Content**:
  - **Name** (Cinzel Bold).
  - **Description** (Italic secondary).
  - **Reaction**: Randomized NPC reaction (e.g., "Suspicious", "Friendly").
  - **Status**: Visual indicator (Fresh ✨, Hit 🩸, Fled 💨, Dead 💀).
- **Edit on click**: Clicking the **Other name** opens the Edit modal.
- **Controls**: All actions are inside a **kebab menu (⋮)** to keep cards compact:
  - Set Status: Fighting ⚔️, Talking 💬, Hit 🩸, Fled 💨, Dead 💀
  - Edit
  - Delete
- **Add Other**: Opens modal to create new entry. Auto-rolls Reaction (2d6).
- **Functionality**:
  - Track status of NPCs/enemies.
  - Status "Hit" indicates damaged/wounded.
  - Status "Dead" fades card.
  - Reaction provides RP prompts.
- **Camp Mode**:
  - Full view.
  - "Mustering" Toggle or "Move" buttons.
  - Edit button.

### Actions Menu

- Located in Header (top right).
- Dropdown or Modal.
- Contains:
  - **Switch to Camp Mode / Switch to Muster Mode**: Toggles UI view.
  - **Export Session**: Downloads `.json`.
  - **Import Session**: Uploads `.json`.
  - **Reset**: Clears session data (with confirmation).

### Character Card

- **Muster Mode**:
  - Compact view.
  - **Header**: Character name with player in parentheses (e.g., `Hawk (Alek)`).
  - **Edit on click**: Clicking the character name opens the Edit Character modal.
  - Hearts/Iron/Arcana adjustment on **one row**.
  - **Stat controls**:
    - Click the stat value to **decrement** (e.g., Hearts -1).
    - Shift-click the stat value to **increment**.
  - **Reorder (Drag & Drop)**:
    - Characters can be dragged to reorder the list.
    - Dropping a character updates **party order numbers** so the displayed order becomes the new order.
    - **Uniqueness**: party order numbers are always **1–n** with **no duplicates**.
    - **Normalization triggers**: applied on drag/drop, manual number edits, and when adding/removing characters from the Muster.
  - **Actions menu (kebab ⋮)**:
    - Edit
    - Delete
    - **Camp** (only shown in Muster mode; moves character to Camp)
  - *No "Move" buttons* (handled in Camp Mode or via Edit).
- **Camp Mode**:
  - Full view.
  - Same name format (`Name (Player)`) and stat row layout.
  - Click name to edit.
  - Drag & drop reordering works within each list (Mustering/Camping) and updates party order numbers.
  - Actions menu (kebab ⋮) replaces inline buttons:
    - Edit
    - Delete
    - **Muster** (only shown for Camping list items; moves character to Mustering)
    - **Camp** (only shown for Mustering list items; moves character to Camping)
  - "Mustering" Toggle or "Move" buttons.
  - Edit button.

---

## Modals

### Character Modal

Title: "Add Character" or "Edit Character"

| Field | Type | Default | Validation |
| --- | --- | --- | --- |
| # (Number) | Number input | Next available | 1-99 |
| Name | Text input | — | Required |
| Description | Textarea | — | Optional |
| Notes | Textarea | — | Optional |
| Hearts (current) | Number input | 7 | 0-20 |
| Hearts (max) | Number input | 7 | 1-20 |
| Iron Hearts (current) | Number input | 0 | 0-10 |
| Iron Hearts (max) | Number input | 0 | 0-10 |
| Arcana Hearts (current) | Number input | 0 | 0-10 |
| Arcana Hearts (max) | Number input | 0 | 0-10 |
| Leader | Checkbox | false | Only one leader allowed |
| Blessed | Checkbox | false | — |

Buttons: Cancel, Save

When editing: current values are editable and are capped at max on save.

When setting leader: removes leader from all other characters.

### Threat Modal

Title: "Add Threat" or "Edit Threat"

| Field | Type | Default | Options |
| --- | --- | --- | --- |
| Name | Text input | — | Required |
| Description | Textarea | — | Optional |
| Level | Number input | — | 0-20, optional |
| Oracle Target | Dropdown | — | —, Easy (6), Normal (8), Hard (10), Extreme (12) |

Buttons: Cancel, Save

---

## Persistence

### localStorage

- Key: `wandyr-session`
- Auto-save on every state change
- Load on page init

### Export

- Filename: `wandyr-session-YYYY-MM-DD.json`
- Pretty-printed JSON (2-space indent)

### Import

- File picker for .json files
- Validates JSON structure
- Replaces entire state
- Handles missing fields gracefully (adds defaults)

---

## Behavior Rules

- **Mode Switching**: User manually toggles between Camp and Muster.
- **Persistence**: `mode` is saved in `localStorage`.
- **Blessing**:
  - When `blessing.active` is true, display the Blessing details in Muster Mode (maybe small in Header or Rumor bar if it persists?). *Correction*: User removed Rumor Bar from Muster spec in prompt, but maybe it should be visible?
  - *Refinement*: User said "In Camp mode, show all characters... enter rumor... obtain blessing".
  - User did *not* say Rumor is hidden in Muster. However, simpler layout suggests keeping Muster focused. Let's assume Rumor/Blessing setup happens in Camp, but effect (buff) is visible in Muster on characters.

### Time Mechanics (Combat)

| Action | Round | Turn | Insight |
| --- | --- | --- | --- |
| + Turn | Reset to 0 | +1 | Roll |
| + Round | +1 | — | Roll |
| Roll Insight | — | — | Roll |

### Insight Values

| Roll | Insight |
| --- | --- |
| 1 | TRAIT |
| 2 | SKILL |
| 3 | ITEM |
| 4 | BYNAME |
| 5 | FEAT |
| 6 | EFFORT |

### Complication Results

| 1s Rolled | Display |
| --- | --- |
| 0 | "All clear" |
| 1 | "Complication!" |
| 2+ | "N× Complication!" |

---

## Future Considerations

- Sound effects for alarm/complication
- Dice rolling animations
- Session history/log
- Multiple saved sessions
- Oracle roller tool
- Random tables integration
- Character sheet links

---

## Changelog

### v1.4 (Current)

- Removed Turn Clock dice (kept Turn + Round + Insight).
- Moved "Where are we?" into the left column to free vertical space for Muster.
- Added Adventure roll card (Easy/Average/Hard).
- Streamlined Others cards: actions in kebab menu.

### v1.3

- Added Camp and Muster Modes.
- Redesigned Header (Title + Actions).
- New Environment Card (Muster).
- New Rumor/Blessing Interface (Camp).
- Moved Export/Import to Actions Menu.
- Updated Data Model for Blessing values.

### v1.2

- Added Camp vs Muster distinction (Lists).
- Added Notes field.
- Mobile-responsive design spec.
- Formalized data model.

### v1.1

- Added initiative numbers.
- Added descriptions to characters and threats.
- Added Oracle target to threats.
- Numeric hearts display (not icons).
- Added Current Rumor and Blessing system (basic).

### v1.0

- Initial implementation
- Turn Clock, Company, Threats
- Hearts as icons
- Basic save/load
