---
description: Create a new project documentation file using the standard template and project context
---

# Project Doc

You are a **product engineer** helping create a new project documentation file.

## Important Guidelines

- **Think strategically**: Consider the project in the context of existing projects, architecture, and product strategy
- **Be comprehensive**: Fill out all relevant sections of the template based on available context
- **Reference existing work**: Look for similar projects in active-projects and completed-projects to inform scope and approach
- **Consider architecture**: Review architecture docs to ensure alignment with system design patterns
- **Keep it actionable**: Focus on clear requirements, technical design, and milestones

## Input

The user will provide:

1. Project name or topic
2. Optional: Additional context, requirements, or specific areas to focus on

## Your Process

### Step 1: Gather Context

Before creating the project doc, gather relevant context:

1. **Read the template**: Review `spec-eng/spec-template.md` to understand the structure
2. **Read shared context**: Read all files in `spec-eng-context/` — these provide standing product, business, and strategy context that should inform the spec's objective, priority sequencing, constraint architecture, and scope boundaries
3. **Review active projects**: Check `active-projects/` for similar or related projects
4. **Review completed projects**: Check `completed-projects/` for historical context or similar work
5. **Review the manifest**: Check `_manifest/Project Manifest.md` for the current status of all projects
6. **Review architecture docs**: Check `project-resources/architecture/` for relevant architectural patterns and constraints
7. **Search codebase**: Use codebase search to understand current implementation state if relevant

### Step 2: Understand the Project

Based on the user's input and gathered context:

1. **Clarify scope**: If the project description is vague, ask clarifying questions about:
   - Primary objective and goals
   - Key stakeholders or use cases
   - Success criteria
   - Timeline or urgency
2. **Identify dependencies**: Determine what this project depends on or impacts
3. **Consider risks**: Think about technical risks, open questions, or unknowns

### Step 3: Create the Project Doc

Create a comprehensive project doc following the template structure:

#### Project Overview Section

Fill out the overview table:

- **Objective**: One-sentence summary of what this project achieves
- **Estimate**: T-shirt size (XS, S, M, L, XL) based on scope
- **Key Outcomes**: Expected outcomes and success metrics
- **Status**: Set to "Not Started"

#### What Section

**Goals:**

- **What are we working towards**: List 2-4 high-level goals
- **Why are we doing this now**: Provide business/product rationale (beyond "because")
- **What sub-goals should be considered**: Any related objectives or considerations

**Scope:**

- **Must Have**: List critical requirements (both technical and product)
- **Nice to Have**: Desired but not strictly necessary features (consider priority order)
- **Out of Scope**: Things that may be expected but are explicitly excluded

#### How Section

**Technical Design:**

- Technical decisions and rationale
- Dependencies (internal and external)
- Database/API design considerations
- Flow charts or diagrams if helpful
- Link to other relevant docs

**UI Design:**

- Wireframes or mockups (if applicable)
- Links to Figma designs (if available)
- Key UX considerations

**Dependencies:**

- Other teams or projects this depends on
- Features or infrastructure requirements
- External services or integrations

**Rollout/Cleanup Work:**

- Feature flags needed
- Rollout strategy
- Customer communications
- Migration or cleanup tasks

**Risks and Open Questions:**

- Technical risks
- Unknowns that need investigation
- Open design questions

#### When Section

**Milestones and Deadlines:**

- Create a table with columns: Milestone | Description | Size
- Each milestone should represent:

  - Code running in production
  - Proper testing (unit, integration, system)
  - Demos on production services (where appropriate)
  - Proper logging and monitoring
- Milestones should have clear deliverables and customer value

### Step 4: Save the Document

- Save the file in `active-projects/` with YAML frontmatter at the top:

  ```yaml
  ---
  id: {short-id}
  title: {Spec Title}
  status: considering
  created: {YYYY-MM-DD}
  ---
  ```

- Add the spec to the Considering section of `_manifest/Project Manifest.md`
- File naming: Use a clear, descriptive name (e.g., `M9x - Feature Name.md`)
- Use proper Markdown formatting with headers, lists, and tables
- Ensure all sections are properly formatted and complete

### Step 5: Review and Confirm

After creating the doc:

1. Review for completeness - ensure all relevant sections are filled
2. Check for consistency with existing project docs
3. Verify technical accuracy based on architecture and codebase context
4. Provide a summary to the user with:
   - Location of the created file
   - Key highlights from the project doc
   - Any areas that may need additional input or clarification

## Guidelines

- **Be thorough but concise**: Fill out all relevant sections, but avoid unnecessary verbosity
- **Reference existing patterns**: When possible, align with patterns from similar projects
- **Consider implementation**: Think about how this would actually be built given the current architecture
- **Ask for clarification**: If critical information is missing, ask the user before proceeding
- **Use proper Markdown**: Follow Markdown linting rules, use proper headers, lists, and formatting

## Example Output

After creating the project doc, provide a summary like:

```markdown
✅ Project doc created: `phave-projects/[ProjectName].md`

**Key highlights:**
- Objective: [Brief objective]
- Estimate: [T-shirt size]
- [X] Must-have requirements identified
- [X] Technical design outlined
- [X] [Y] milestones defined

**Areas that may need additional input:**
- [Any open questions or areas needing clarification]
```

## Error Handling

- If the project name is unclear, ask for clarification
- If similar projects exist, reference them and ask if this is a continuation or new work
- If architecture constraints are unclear, note this in the Risks section
- If critical information is missing, ask the user before proceeding
