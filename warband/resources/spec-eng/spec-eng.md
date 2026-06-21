# Specification Engineering

This is my process for writing specs and having Claude Code implement them autonomously.

A spec is not a prompt. A prompt is a one-shot instruction. A spec is a durable artifact that an autonomous agent can execute against — with constraint architecture, failure modes, and a definition of done — over hours or days without hand-holding.

---

## The Lifecycle

All specs live in `active-projects/`. Status is tracked in two places: the Project Manifest (`_manifest/Project Manifest.md`) and the spec's YAML frontmatter (`status:` field). The manifest is the master source — change status there, then run `/manifest` to push changes into spec frontmatter.

```text
considering → intended → implementing → evaluating → deploying → shipped
```

The bottlenecks are thinking, reviewing, evaluating, and deploying — everything except drafting, implementing, and communicating. Implementation is not the bottleneck.

**Blocked** is not a lifecycle stage — it's a cross-cutting state that can happen at any stage. Handle it as a note within the spec, not as a folder.

### Think

Before opening any AI session, work through the **Human Prompt** — seven questions, pen and paper, no AI. The purpose is to get your thinking out of your head before AI has a chance to reshape it.

AI is too fluent. You say something half-formed. It hands you back a polished, confident version. You adopt its framing instead of finishing your own. Pen and paper don't have opinions.

**The seven questions:**

- **What am I actually trying to accomplish?** The outcome, not the task. One sentence. "Implement recipient tokens" is a task. "Let email authors reference who an email is being sent to, discoverable directly in the editor" is an outcome.
- **Why does this matter?** What happens if it goes well? What happens if you skip it?
- **What does "done" look like?** The finished output. Specific.
- **What does "wrong" look like?** The subtle failure modes — what would make you say "no, that's not what I meant" even if it's polished and technically correct. *This is the one people skip. It is the most important.*
- **What do I already know that I haven't written down?** Institutional knowledge, unwritten rules, context obvious to you but not to someone new.
- **What are the pieces?** Decomposition. Components, subtasks, dependencies.
- **What's the hard part?** Where the judgment calls are. Where it could go sideways. Where you're least certain.

### Draft → `considering`

Use the `/spec` slash command to create a spec from the template. The slash command reads any shared context files in `spec-eng-context/` before drafting — these provide standing product, business, and strategy context that should inform the spec without being duplicated into it. The Human Prompt answers map directly to spec sections:

- Outcome → **Objective**
- Why it matters → **Why Now**
- Done → **Priority Queue "Done when" criteria**
- Wrong → **Constraint Architecture + Failure Modes**
- Unwritten knowledge → **Agent Technical Context**
- Pieces → **Priority Queue sequencing**
- Hard part → **Risks and Open Questions**

The slash command will remind you to do the Human Prompt first, then guide you through constraint architecture and failure modes — the questions most people skip. The new spec is saved to `active-projects/` with `status: considering` in its frontmatter, and added to the Considering section of the Project Manifest.

### Review → stays `considering`

Two review passes, in order:

**Spec Rating** — Run the `/rate` slash command. This scores the spec against the 7-dimension rubric (self-contained problem statement, priority queue, constraint architecture, failure modes, risks, agent technical context, comms). Target: 9/10 in every dimension. Below 9 triggers a question-and-answer remediation loop to surface missing information. This catches structural gaps — thin failure modes, empty risks, missing constraints.

**Pre-Implementation Review** — Read all CLAUDE.md files in each affected repo. The Pre-Implementation section uses adversarial evaluation: a Critic argues the spec is wrong (missing constraints, unclear criteria, scope problems, CLAUDE.md inconsistencies) while a Defender argues it's correct. This catches logical issues that a single balanced review would hedge past. The spec stays `considering` until it passes both rating and review.

Read the reviews. This is the second bottleneck — you must actually read them.

### Commit → `intended`

Set the spec's status to `intended` and move it to the Intended section of the manifest. Revise the **"I Intend To"** comms text if scope changed since drafting. Marking a spec intended means you're committing to the work. Post when you commit.

### Implement → `implementing`

Set the spec's status to `implementing` and move it in the manifest. Use the `/implement` slash command with the spec name. Claude reads the spec and executes against it, Priority Queue top-down. For larger projects, implement one priority queue item at a time.

### Evaluate → `evaluating`

Set the spec's status to `evaluating` and move it in the manifest. Read all CLAUDE.md files in each affected repo. The Post-Implementation review uses the same adversarial evaluation: a Critic argues the implementation doesn't match the spec (including CLAUDE.md compliance) while a Defender argues it does. Tightly-scoped bugs get fixed. Large-scale issues become new specs.

Read the review. This is the third bottleneck.

### Deploy → `deploying`

Set the spec's status to `deploying` and move it in the manifest. Create the PR, review it, merge, deploy, verify in production. This is the last human bottleneck before the work is done.

### Ship → `shipped`

Revise the **"I Shipped"** comms text if scope changed during implementation. Set the spec's status to `shipped` and move it to the Done / Shipped section of the manifest. Optionally move the spec file to `completed-projects/`. Post when the investment pays off.

Then score the spec against the eval harness — three questions:

- **Did the pre-implementation review catch a real issue?** If yes, the Constraint Architecture or Risks section worked. If not, either the spec was clean or the review missed something — check which.
- **Did "technically correct but wrong" happen anyway?** If yes, there was a missing constraint or failure mode. Write down what it was. This is the most valuable signal — it tells you what the spec template failed to prompt you for.
- **Were there surprises the spec should have anticipated?** Things that came up during implementation that the spec didn't address. These are gaps in self-containedness.

Log the scores at `spec-eng/eval-log.md`. One entry per shipped spec — the spec name, the three scores (yes/no with a brief note), and any template or process change the experience suggests. Review the log quarterly and after model updates. This is the feedback loop that tells you whether specs are getting more self-contained or the same gaps keep recurring.

---

## What a Spec Contains

A spec has two halves. The top half is human-readable — optimized for writing and reviewing. The bottom half is agent-readable — optimized for Claude Code. The full template is at `spec-eng/spec-template.md`.

### Human-readable (top half)

**Objective** — The outcome in one to three sentences. Not the task — the outcome. Self-contained: a reader should understand what's being built and why without asking questions.

**Why Now** — The triggering reason. What happens if this ships? What happens if it doesn't? How does this connect to the principles, strategy, or goals that govern your work? This is where alignment lives — not as a separate section, but as part of articulating why this matters now.

**Priority Queue** — The sequencing. Items ship top-down. Each item has a description and **"Done when"** acceptance criteria. Position is priority — no T-shirt sizes, no sprint estimates.

**Constraint Architecture** — The four-quadrant framework that prevents "technically correct but wrong":

- **Musts** — non-negotiable requirements. Violation means the output is wrong.
- **Must-Nots** — explicit prohibitions. Things the output must never do or include.
- **Preferences** — desired but not required. Tradeoffs the executor can make.
- **Escalation Triggers** — conditions where the executor should stop and ask rather than guess.

**Failure Modes** — What would make you say "no, that's not what I meant" even if the output is polished? The subtle ways a competent executor could satisfy every stated requirement but produce the wrong outcome. Concrete examples over abstract descriptions.

**Out of Scope** — What not to build. Each item should be promotable to its own spec. This prevents scope creep by the AI.

**Risks and Open Questions** — Where the hard parts live. Judgment calls, ambiguity, things that could go sideways. This is where the spec needs the most detail and where people provide the least.

**Comms** — Four slots, all written when drafting the spec. Revise at the appropriate lifecycle transition if scope changed during implementation. Writing comms early forces you to articulate the value before building — if you can't explain what shipped and why it matters, the spec isn't ready.

- **I Intend To** — Posted when you commit to the work. 2-3 sentences max. Lead with the spec name, connect to the broader narrative (e.g., correctness, trust, reliability), then one sentence on the problem being fixed. Keep the tone upbeat and vary the structure — don't open every post the same way.
- **I Shipped** — Posted when the investment pays off. 2-3 sentences max. Lead with what changed for customers, not implementation details. Upbeat — this is a win. Vary the framing across specs.
- **GTM Announcement** — What the GTM team needs to know — the new stories they can spin, the value proposition for prospects and existing customers.
- **Tenant Announcement** — What marketing ops and demand-gen marketers (your tenants) need to know about what changed and how it affects their workflows. May be delivered verbally by the GTM team rather than written directly to tenants — the comms text here is the source material either way.

**Review** — Pre-Implementation (is this the correct spec?) and Post-Implementation (is this the correct implementation?). Both start by reading all CLAUDE.md files in affected repos, then use adversarial evaluation: a Critic finds problems (including CLAUDE.md inconsistencies) while a Defender argues for correctness. The tension between them surfaces issues that a single balanced review would hedge past.

### Agent-readable (bottom half)

**Agent Technical Context** — Everything Claude Code needs to implement: current architecture context, implementation approach, file references, dependencies, rollout plan. This section opens with "Humans: stop reading here." It is optimized for machine consumption and not expected to be read by humans.

---

## Key Principles

### Self-contained problem statements

Every spec must be a fully self-contained problem statement. The executor — human or AI — should be able to understand what to build, why, and what the constraints are without asking clarifying questions or consulting external context. If the spec requires information that's in the author's head but not in the document, it is not self-contained.

Self-contained does not mean context-free. Shared context files in `spec-eng-context/` — product principles, business strategy, standing constraints — should inform spec decisions (objective framing, priority sequencing, scope boundaries) without being restated. The spec references the context; the context informs the judgment.

### Constraint architecture earns its place

The single highest-leverage addition to any spec is the Constraint Architecture section. Most specs capture what "done" looks like but not what "wrong" looks like. The result is the "technically correct but wrong" pattern: AI delivers output that checks every box but misses the intent because the constraints were implicit, not explicit.

The M9w Quiet Hours spec is a concrete example from this codebase — the proposed "phase 4" architecture satisfied every stated requirement but would have reintroduced limit violations, which wasn't captured as a constraint.

### Lightweight over thorough

Every section a human must read should earn its place. If the template feels like paperwork — filling in sections because they exist — it has failed. The spec should feel like the cheapest way to catch mistakes before they're in code.

Technical detail (file paths, code references, task breakdowns) goes in Agent Technical Context, not in the human-readable sections. The reviewer — often you, on your phone — needs to quickly assess whether the spec captures the right intent without wading through implementation detail.

### Adversarial evaluation over single-agent review

When evaluating work — "is this spec correct?", "is this implementation right?", "did we miss anything?" — use two agents with opposing roles: a **Critic** whose job is to find problems, and a **Defender** whose job is to argue for correctness. A single agent asked to "argue for and against" produces hedged, balanced output. Two agents with clear roles produce genuine tension that surfaces real issues.

This applies to any evaluation question, not just the spec review gates. If you're asking an AI "is this right?", the answer is more trustworthy when one agent is incentivized to say no.

### A spec is not a prompt

A prompt is a one-shot instruction. A spec is a durable artifact with constraint architecture, failure modes, and a definition of done. If specs degrade into long prompts, the process has failed. The distinguishing features: a spec has a Priority Queue (sequencing), Constraint Architecture (what wrong looks like), Review gates (pre and post implementation), and Agent Technical Context (enough context for autonomous execution).

---

## Tools and Files

### Slash commands

- `/spec` — Create a new spec from the template. Reminds you to do the Human Prompt first. Guides you through constraint architecture and failure modes.
- `/upgrade-spec` — Convert an old-format project doc to the current spec-eng template. Pass the spec file path as the argument.
- `/rate` — Rate a spec against the 7-dimension rubric. Scores each dimension 1-10. Below 9 triggers remediation questions. Run during Review, before pre-implementation review.
- `/implement` — Implement a named spec. Reads the spec, runs pre-implementation review, executes Priority Queue top-down, runs post-implementation review.
- `/manifest` — Sync status from the Project Manifest into spec file frontmatter. Highlight specific lines in the manifest to update only those specs, or run without arguments to sync all.
- `/intend` — Generate the "I Intend To" and "I Shipped" posts by scanning specs with `status: intended` for intent comms and `status: shipped` for recently shipped comms.

### File locations

- **This process:** `spec-eng/spec-eng.md`
- **Spec template:** `spec-eng/spec-template.md`
- **Human Prompt starter:** `spec-eng/spec-starter.md`
- **Spec creation prompt:** `spec-eng/spec-prompt.md`
- **Spec rating prompt:** `spec-eng/spec-rating-prompt.md`
- **Eval log:** `spec-eng/eval-log.md`
- **Prompt Kit reference:** `spec-eng/Prompt Kit - You're Prompting Like It's Last Month.md`
- **Shared context:** `spec-eng-context/` — Product principles, personal preferences, values, company standards, and other general context that applies to every spec

### Status tracking

- **`active-projects/`** — All specs in flight, regardless of stage
- **`completed-projects/`** — Shipped specs, organized by time period
- **`_manifest/Project Manifest.md`** — Master list of all projects, sectioned by status

Status values in spec frontmatter: `considering`, `intended`, `implementing`, `evaluating`, `deploying`, `shipped`.

- **"I Intend To" log:** `I Intend To.md` — Historical aggregation of "I Intend To" and "I Shipped" posts, sourced from individual spec Comms sections

All paths are relative to the `_projects/` directory.

---

## Background: The Four Disciplines

This process is grounded in the framework from Nate Jones's article "Prompting just split into 4 different skills." Prompting has split into four disciplines that build on each other:

**Prompt Craft** → **Context Engineering** → **Intent Engineering** → **Specification Engineering**

This process operates primarily in the fourth discipline but draws on the others:

- **Context Engineering** is about loading the right context so the AI doesn't guess. The Agent Technical Context section of a spec serves this purpose for a specific project. CLAUDE.md and memory files serve it across all projects. Shared context files in `spec-eng-context/` serve it at the product level — standing principles and strategy that apply to every spec.
- **Intent Engineering** is about encoding judgment — tradeoffs, decision-making rules, escalation triggers. The Constraint Architecture and Failure Modes sections encode intent for a specific project.
- **Specification Engineering** is the full discipline: writing a document complete enough that an autonomous agent can execute against it for hours or days without human intervention.

<!-- markdownlint-disable MD013 MD024 -->
