# Wåndyr Session Dashboard Specification

Version: 1.3
Date: January 4, 2026

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
    "hour": 0,
    "clock": 0,
    "insight": 0
  },
  "environment": {
    "region": "Wåndyrwyld",
    "terrain": "forest",
    "weather": "clear",
    "weather": "clear",
    "weatherDice": [3, 4, 1]
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
- **Turn Clock**: Standard clock tracking.
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
│ ENVIRONMENT CARD: Region | Terrain | Weather | Dice         │
├──────────────┬─────────────────────────┬────────────────────┤
│  TURN CLOCK  │      THE MUSTER         │      THREATS       │
│              │                         │                    │
│  ○ ○ ○ ○ ○ ○ │  [Character Cards]      │  [Threat Cards]    │
│              │                         │                    │
│  Round: 0    │                         │                    │
│  Turn: 0     │                         │                    │
│  Hour: 0     │                         │                    │
│  Clock: 0    │                         │                    │
│              │                         │                    │
│  ┌────────┐  │                         │                    │
│  │ SKILL  │  │                         │                    │
│  └────────┘  │                         │                    │
│              │                         │                    │
│ [+Turn]      │                         │  [+ Add Threat]    │
│ [+Round]     │                         │                    │
│ [Roll Clock] │                         │                    │
│ [Reroll]     │                         │                    │
│              │                         │                    │
│ Roll Result  │                         │                    │
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
- **Terrain**: Dropdown (Forest, Mountains, Swamp, Desert, Plains, Urban, Underground, Coastal).
- **Weather**: Dropdown (Clear, Cloudy, Rain, Storm, Fog, Snow, Extreme Heat, Extreme Cold).
- **Weather Dice**: Visual pip faces (3 dice). "Roll" button.

### Rumor & Blessing (Camp Mode)
- **Rumor**: Text area.
- **Blessing**:
    - **Source**: Text Input (e.g., "The Forest Spirit").
    - **Value**: Number Input (e.g., 2).
    - **Active**: Checkbox/Toggle.
    - *Effect*: When active, characters marked as 'Blessed' receive a visual cue (Gold Glow). The 'Value' is for reference by the Guide (e.g., "You all have 2 extra Iron Hearts").

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
    - Hearts/Iron/Arcana adjustment.
    - Edit button.
    - *No "Move" buttons* (handled in Camp Mode or via Edit).
- **Camp Mode**:
    - Full view.
    - "Mustering" Toggle or "Move" buttons.
    - Edit button.

---

## Modals

### Character Modal

Title: "Add Character" or "Edit Character"

| Field | Type | Default | Validation |
|-------|------|---------|------------|
| # (Number) | Number input | Next available | 1-99 |
| Name | Text input | — | Required |
| Description | Textarea | — | Optional |
| Notes | Textarea | — | Optional |
| Hearts (max) | Number input | 7 | 1-20 |
| Iron Hearts (max) | Number input | 0 | 0-10 |
| Arcana Hearts (max) | Number input | 0 | 0-10 |
| Leader | Checkbox | false | Only one leader allowed |
| Blessed | Checkbox | false | — |

Buttons: Cancel, Save

When editing: current values preserved for hearts/iron/arcana (capped at new max).

When setting leader: removes leader from all other characters.

### Threat Modal

Title: "Add Threat" or "Edit Threat"

| Field | Type | Default | Options |
|-------|------|---------|---------|
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

### Time Mechanics

| Action | Round | Turn | Clock | Hour | Insight |
|--------|-------|------|-------|------|---------|
| + Turn | Reset to 0 | +1 | +1 | +1 if clock was 5 | Roll |
| + Round | +1 | +1 if rounds hit 60 | +1 if turn incremented | (cascade) | Roll |
| Roll Clock | — | — | — | — | — |
| Reroll | — | — | — | — | Roll |

### Clock Overflow

When clock reaches 6:
1. Roll all 6 dice
2. Count 1s, display result
3. Clear clock to 0
4. Increment hour

### Insight Values

| Roll | Insight |
|------|---------|
| 1 | TRAIT |
| 2 | SKILL |
| 3 | ITEM |
| 4 | BYNAME |
| 5 | FEAT |
| 6 | EFFORT |

### Complication Results

| 1s Rolled | Display |
|-----------|---------|
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

### v1.3 (Current)
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
