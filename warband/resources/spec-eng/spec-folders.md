# Spec Artifact Folders

## Convention

Each spec is a single self-contained markdown file. When a spec requires supporting
material or produces deliverables, two optional sibling folders extend it:

``` text
M9e - Quiet Hours.md
M9e - Quiet Hours.input/     ← optional: files feeding into the work
M9e - Quiet Hours.output/    ← optional: files produced by the work
```

The spec file and its artifact folders share the same base name (`M9e - Quiet Hours`)
and live as siblings within the same stage folder. The `.input` / `.output` suffix uses
a dot delimiter so it cannot collide with hyphens or spaces in the spec name. Neither
folder is created unless needed.

When a spec moves between lifecycle stages, its artifact folders move with it.

---

## Folder Semantics

### `[spec].input/`

Contains material that informs implementation. Claude Code reads this folder.

Examples:

- UX mocks and screenshots
- Sample JSON or CSV data
- API contracts and schema files
- Research notes and reference documents
- Design decisions too large to embed in the spec

### `[spec].output/`

Contains deliverables produced by the work. Claude Code writes here.

Examples:

- Action plans and implementation outlines
- Exported reports or structured data files
- Generated documentation
- Any artifact delivered to a human rather than merged into the codebase

---

## Presence as Signal

The existence of a folder is itself meaningful:

| State | Meaning |
|---|---|
| No folders | Self-contained spec — the common case (~80%) |
| `.input/` present | Spec requires supporting material to implement |
| `.output/` present | Spec produces human-deliverable artifacts |
| Both present | Complex spec with supporting material and deliverables |

Claude Code can infer read/write intent from folder name alone, without reading the spec.

---

## What Does Not Belong Here

**Implementation artifacts** (code, PRs, branches) live in the code repository. The spec
references them by name or link — it does not contain them.

**Process notes** (evaluation observations, test results) belong inline in the spec
itself, not in an artifact folder.

---

## Example

Observe how specs are always at the same level as their artifact folders, never nested inside them:

``` text
    M9a - Cache Warmup.md
    M9c - Rate Limiting.md
    M9e - Quiet Hours.md
    M9e - Quiet Hours.input/
      contract.md
      sample-payload.json
      ux-mock.png
    M9g - Report Builder.md
    M9g - Report Builder.output/
      action-plan.md
      summary-report.md
    M9t - Schema Migration.md
```
