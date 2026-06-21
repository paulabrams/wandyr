# Spec Rating Prompt

Rate a spec against the specification engineering rubric. This prompt is self-contained — it embeds the scoring criteria derived from the Prompt Kit framework and the spec-eng process so ratings are consistent across sessions.

## Instructions

Read the spec being rated. Score each dimension below on a 1-10 scale. Provide a brief justification for each score — what's strong, what's missing. Then give an overall score.

## Scoring Dimensions

### 1. Self-Contained Problem Statement

Does the Objective + Why Now form a complete, self-contained problem statement? Can a reader unfamiliar with the project understand what's being built and why without asking questions?

- **9-10:** Outcome-focused objective (not task-oriented). Clear stakes framing (if this ships / if it doesn't). A new reader understands the project without consulting external context. Where shared context exists (e.g., product principles, business strategy in `spec-eng-context/`), the spec's framing is consistent with it.
- **7-8:** Objective is clear but task-oriented ("Implement X" rather than "Enable Y"). Why Now is present but doesn't articulate stakes.
- **5-6:** Objective exists but requires context to understand. Why Now is missing or generic.
- **1-4:** Objective is a task list. No Why Now. Reader must ask questions to understand what's being built.

### 2. Priority Queue and Definition of Done

Are the pieces identified and sequenced? Does each item have specific "Done when" acceptance criteria?

- **9-10:** Clear sequencing. Each item has specific, testable Done-when criteria. Position is priority. No ambiguity about what's in scope.
- **7-8:** Items are listed with Done-when criteria, but some are vague ("works correctly") or untestable.
- **5-6:** Items exist but lack Done-when criteria or clear sequencing.
- **1-4:** No priority queue, or items are a flat list without criteria.

### 3. Constraint Architecture

Does the spec encode what "wrong" looks like using the four-quadrant model?

- **Musts** — Non-negotiable requirements. Violation means the output is wrong.
- **Must-Nots** — Explicit prohibitions. Things the output must never do.
- **Preferences** — Desired but flexible. Tradeoffs the executor can make.
- **Escalation Triggers** — Conditions where the executor should stop and ask.

Scoring:

- **9-10:** All four quadrants populated with specific, actionable items. Constraints are testable. Preferences include explicit tradeoff ordering. Escalation triggers name real scenarios.
- **7-8:** Three or four quadrants populated, but some items are generic or obvious. Escalation triggers may be thin.
- **5-6:** One or two quadrants populated. Constraints exist but are mostly restating the Priority Queue in negative form.
- **1-4:** No constraint architecture, or only a vague "don't over-engineer" note.

### 4. Failure Modes

Does the spec name the subtle ways a competent executor could satisfy every stated requirement but produce the wrong outcome? This is the "technically correct but wrong" question — the one people skip.

- **9-10:** Concrete failure modes covering both implementation behavior and user-facing impact. Each mode names what goes wrong and why it's not obvious. At least one references a real past experience. For shipped specs: annotates when issues were caught (review, implementation, production).
- **7-8:** Failure modes exist but are all one type (all implementation-focused or all user-facing). Modes are real but generic.
- **5-6:** One or two failure modes that restate Must-Nots as scenarios rather than naming genuinely subtle problems.
- **1-4:** No failure modes section, or only "it could be slow."

### 5. Risks and Hard Parts

Does the spec name where the judgment calls are — where it could go sideways, where the author is least certain? For shipped specs: does it preserve the institutional knowledge of what was hard and why?

- **9-10:** Names specific hard parts with context on why they're hard. For shipped specs: retrospective captures the judgment calls that were resolved, with enough context for a future reader to understand the decision and its reasoning.
- **7-8:** Risks are named but without context on why they're hard or how they were resolved.
- **5-6:** Generic risks ("this is complex") without specifics.
- **1-4:** No risks section, or "no risks identified."

### 6. Agent Technical Context

Is the bottom half dense enough for autonomous execution? Could an agent pick up the remaining work (or maintenance) from a cold start without asking clarifying questions?

- **9-10:** Architecture context, file paths, implementation approach, algorithm steps, data types, dependencies — all present. Clear separation from human-readable top half. An agent can execute without external context.
- **7-8:** Technical context exists but has gaps (missing file paths, vague implementation approach, or stale references).
- **5-6:** Technical details are mixed into the human-readable sections rather than compartmentalized.
- **1-4:** No agent context, or only a few file paths.

### 7. Comms

Are all four slots drafted with audience-appropriate content? Comms are written at draft time, not deferred — if the author can't articulate what shipped and why it matters, the spec isn't ready.

- **I Intend To** — Posted when you commit to the work. 2-3 sentences, upbeat, varied structure across specs.
- **I Shipped** — Posted when the investment pays off. 2-3 sentences, upbeat, customer-outcome-first.
- **GTM Announcement** — What the GTM team needs to know.
- **Tenant Announcement** — What marketing ops and demand-gen marketers need to know.

Scoring:

- **9-10:** All four slots drafted at spec creation time. Each is written for its audience (not copy-pasted across slots). I Intend To and I Shipped are 2-3 sentences, upbeat, and varied in structure across specs (not formulaic). GTM focuses on value proposition and stories. Tenant focuses on what changed and how it affects workflows. Slots marked N/A with a reason (e.g., internal process improvement) count as drafted.
- **7-8:** Three or four slots populated, but some are generic, audience-inappropriate, or are placeholders deferred to a later lifecycle stage.
- **5-6:** One or two slots populated, or all four are placeholders.
- **1-4:** No comms section.

## Output Format

For each dimension, output:

```text
### [Dimension Name]: [Score]/10
[2-3 sentences: what's strong, what's missing or could improve]
```

Then:

```text
### Overall: [Score]/10
[1-2 sentences summarizing the spec's strongest quality and biggest gap]
```

## Success and Remediation

**Success** is a rating of 9/10 or above overall and in each dimension.

**Below 9** in any dimension: ask the spec author targeted questions to surface the missing information — the way the Human Prompt's seven questions surface thinking that hasn't been written down yet. Use multi-select questions when appropriate. After each round of answers, update the spec and re-score the improved dimensions. Repeat until all dimensions reach 9/10.
