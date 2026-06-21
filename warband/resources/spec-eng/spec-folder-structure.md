# Spec Folder Structure

## Top-Level Layout

```text
_manifest/
  Project Manifest.md
active-projects/
completed-projects/
```

`active-projects/` holds all specs that are in flight — regardless of stage. `completed-projects/` holds specs that shipped, organized by time period. Status lives in two places: the **Project Manifest** (the master source of truth) and each spec's **YAML frontmatter** (a local copy kept in sync via `/manifest`).

---

## How Status Works

### The Manifest

`_manifest/Project Manifest.md` is the single-pane view of all projects. It has sections ordered to facilitate getting work in process to done:

| Section | Meaning |
|---|---|
| Deploying | PR, code review, merge, deploy, verify in production |
| Evaluating | Formal acceptance review against spec definition of done |
| Implementing | Claude Code actively working |
| Intended | Committed to the work — "I Intend To" posted |
| Considering | Drafting and pre-implementation review |
| Done / Shipped | Historical record, organized by quarter |

Work from the top of the manifest down. Within a section, order is priority / sequencing.

### Spec Frontmatter

Each spec file carries its own status in YAML frontmatter at the top:

```yaml
---
id: M9te
title: Tactic Entry Limits
status: considering
created: 2026-03-15
---
```

| Field | Description |
| --- | --- |
| `id` | Short identifier for the spec (e.g., `M9te`, `UPS1`). Used as a stable reference across the manifest and other docs. |
| `title` | Human-readable spec title. Matches the `# heading` in the spec body. |
| `status` | Current lifecycle stage. Valid values: `considering`, `intended`, `implementing`, `evaluating`, `deploying`, `shipped`. |
| `created` | Date the spec was first drafted (`YYYY-MM-DD`). |

### Changing Status

To change a spec's status:

1. Move the spec's entry to the appropriate section in the Project Manifest
2. Run `/manifest` to push the status change into the spec's YAML frontmatter

The manifest is the master source. The frontmatter is a local copy. The `/manifest` command keeps them in sync.

---

## Stage Transitions

Each transition has meaning:

- **considering -> intended** — committed to the work
- **intended -> implementing** — work has started
- **implementing -> evaluating** — stepping out of build mode to make a binary judgment against the spec
- **evaluating -> implementing** — return to build mode (failed evaluation)
- **evaluating -> deploying** — committed to ship; post "I Intend To"
- **deploying -> shipped** — shipped; post "I Shipped"

### Implementing vs Evaluating

These are distinct modes, not a continuous loop:

**Implementing** covers the tight working loop — delegate to Claude Code, check output,
fix, repeat. This is still implementation. The spec is not done.

**Evaluating** is a deliberate pause. Step back. Hold the output against the spec's
definition of done and constraint architecture. Make a binary judgment: pass or return
to implementing. This is a true phase gate, not just more iteration.

---

## Communications

Both comms bracket the shipping event:

- **Enter deploying** -> post "I Intend To"
- **deploying -> shipped** -> post "I Shipped"

"I Intend To" is not tied to a calendar day. It is posted when you are genuinely ready
to commit publicly — which may be hours or days before "I Shipped". The gap between
the two comms is event-driven, not calendar-driven.

---

## Shipped Specs

When a spec ships, it stays in `active-projects/` with `status: shipped` in its frontmatter and moves to the Done / Shipped section of the manifest. Optionally, the spec file can be moved to `completed-projects/` organized by time period (e.g., `completed-projects/2026-q1/`).

Shipped specs are **ground truth** — they describe code that exists in production. Claude Code should treat content here as authoritative reality.

---

## Spec Artifact Folders

See `spec-eng/spec-folders.md` for the full convention on `.input/` and `.output/` sibling folders.

---

## Full Reference

```text
_manifest/
  Project Manifest.md
active-projects/
  M9a - Cache Warmup.md                   (status: shipped)
  M9c - Rate Limiting.md                  (status: considering)
  M9e - Quiet Hours.md                    (status: implementing)
  M9e - Quiet Hours.input/
    contract.md
    sample-payload.json
    ux-mock.png
  M9g - Report Builder.md                 (status: evaluating)
  M9g - Report Builder.output/
    action-plan.md
    summary-report.md
  M9t - Schema Migration.md               (status: intended)
completed-projects/
  2026-q1/
    M9b - Send Test Email.md
```
