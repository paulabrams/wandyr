---
id: {short-id}
title: {Spec Title}
status: considering
created: {YYYY-MM-DD}
---

# {Spec Name}

## Objective

{The outcome in one to three sentences. Not the task — the outcome. Self-contained: a reader should understand what's being built and why without asking questions.}

## Why Now

{The triggering reason. What happens if this ships? What happens if it doesn't? How does this connect to the principles, strategy, or goals that govern your work?}

---

## Priority Queue

> Items ship top-down. Position is priority — no labels, no estimates. Lower items may not ship if capacity is consumed by higher items.

### {Item Name}

{description}

**Done when:** {acceptance criteria}

### {Item Name}

{description}

**Done when:** {acceptance criteria}

---

## Constraint Architecture

### Musts

{Non-negotiable requirements. Violation means the output is wrong.}

### Must-Nots

{Explicit prohibitions. Things the output must never do or include.}

### Preferences

{Desired but not required. Tradeoffs the executor can make.}

### Escalation Triggers

{Conditions where the executor should stop and ask rather than guess.}

---

## Failure Modes

{What would make you say "no, that's not what I meant" even if the output is polished? The subtle ways a competent executor could satisfy every stated requirement but produce the wrong outcome. Concrete examples over abstract descriptions.}

---

## Out of Scope

> Each item here should be promotable to its own spec. This prevents scope creep by the AI.

### {Out of Scope Item}

{description}

---

## Risks and Open Questions

### {Risk or Question}

{description}

---

## Comms

> Write all four slots when drafting the spec. Revise at the appropriate lifecycle transition if scope changed during implementation.

### I Intend To

{2-3 sentences max. Lead with the spec name, connect to the broader narrative (e.g., correctness, trust, reliability), then one sentence on the problem being fixed. Upbeat, varied — don't open every post the same way.}

### I Shipped

{2-3 sentences max. Lead with what changed for customers, not implementation details. Upbeat — this is a win. Vary the framing across specs.}

### GTM Announcement

{What the GTM team needs to know — the new stories they can spin, the value proposition for prospects and existing customers.}

### Tenant Announcement

{What marketing ops and demand-gen marketers (your tenants) need to know about what changed and how it affects their workflows.}

---

## Review

### Pre-Implementation

**Before starting implementation:** Read all CLAUDE.md files in each affected repo. Then use adversarial evaluation to answer "Is this the correct spec?" Write the results below this paragraph.

**Critic:** Argue this spec is wrong. Find missing constraints, unclear acceptance criteria, scope problems, unstated assumptions, and failure modes the spec didn't anticipate. Verify the spec is consistent with CLAUDE.md instructions. Be specific — name what's missing and why it matters.

**Defender:** Argue this spec is correct. Explain why the objective, constraints, and priority queue are sufficient. Address the Critic's concerns directly — either rebut them or acknowledge them as genuine gaps.

If there are minor issues such as typos, fix them. Do not implement any large-scale changes or new features at this time.

### Post-Implementation

**After finishing implementation:** Read all CLAUDE.md files in each affected repo. Then use adversarial evaluation to answer "Is this the correct implementation?" Write the results below this paragraph.

**Critic:** Argue the implementation doesn't match the spec. Find deviations from acceptance criteria, constraint violations, edge cases not handled, and "technically correct but wrong" patterns. Verify all CLAUDE.md instructions were followed. Review the actual code, not just the intent.

**Defender:** Argue the implementation is correct. Explain how each priority queue item's Done-when criteria are met. Address the Critic's concerns directly.

If there are tightly-scoped bugs then fix them. Do not implement any large-scale changes or new features at this time.

When editing tenant-portal files, always check for lint errors using `pnpm run -r lint`.

---

## Agent Technical Context

> Humans: stop reading here. Everything below is optimized for Claude Code.

{Everything Claude Code needs to implement: current architecture context, implementation approach, file references, dependencies, rollout plan.}

<!-- markdownlint-disable MD013 MD024 -->
