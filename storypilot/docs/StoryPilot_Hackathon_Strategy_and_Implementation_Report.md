# StoryPilot: Evidence-Driven Software Story Intelligence

## Hackathon Strategy, Problem Analysis, Product Specification, Architecture, and Implementation Plan

**Document type:** Project strategy and technical implementation report\
**Project:** StoryPilot\
**Proposed hackathon theme:** Future of Work & Enterprise Productivity\
**Target platform:** Google Cloud\
**AI requirement:** Google AI models (Gemini/Gemma) and/or qualifying
Google agentic platforms\
**Deployment target:** Cloud Run or Firebase\
**Status:** Proposed plan; validate final event rules, available APIs,
and submission deadline before implementation.

------------------------------------------------------------------------

# Executive Summary

StoryPilot is an AI co-pilot for the lifecycle of a software engineering
story: from assignment and context gathering through clarification,
implementation evidence, and documentation. It targets a familiar but
costly source of engineering friction: information needed to complete a
task is scattered across work items, technical documentation, code, pull
requests, decisions, emails, and support records.

The central product principle is **"capture once, reuse everywhere."** A
canonical story record stores the story's requirements, source evidence,
open questions, decisions, activity, implementation evidence, and
documentation state. Multiple outputs---context briefs, clarification
requests, traceability matrices, completion documentation, status
summaries, and optional timesheet drafts---are derived from that shared
record rather than maintained independently.

The broad vision can cover seven stages:

1.  Story assigned.
2.  Context brief assembled.
3.  Requirement gaps detected and clarification questions prepared.
4.  Work activity captured.
5.  Pre-PR checks and evidence review.
6.  Completion documentation drafted.
7.  Status summaries and optional timesheet drafts generated.

The hackathon MVP should **not** attempt to fully automate all seven
stages. The recommended scope is:

-   **Core:** evidence-linked context brief.
-   **Core:** missing or contradictory requirement detection.
-   **Core:** acceptance-criteria-to-evidence traceability.
-   **Core:** documentation draft generated from approved story details
    and a supplied code diff.
-   **Supporting:** human approval queue and audit trail.
-   **Optional:** clarification workflow and activity summary.
-   **Roadmap only:** live integrations with every work tool, Fortify
    triage, automated production issue intake, advanced release
    prediction, and timesheet submission.

The proposed positioning is:

> **StoryPilot: an AI co-pilot that turns fragmented engineering context
> into evidence-linked briefs, exposes requirement gaps before coding,
> and keeps completion documentation aligned with the change.**

The main competitive opportunity is not "another AI chatbot" or "a
collection of agents." It is a verifiable workflow that connects a
story, the evidence supporting it, the requirements still unresolved,
and the final documentation.

The initial concept receives a subjective strategic rating of
**8.3/10**, with a focused MVP rated substantially more feasible than
the full lifecycle vision. These ratings are internal planning
judgments, not official organizer scores or a guarantee of winning.

------------------------------------------------------------------------

# 1. Hackathon Context and Primary Constraints

## 1.1 Primary objective

The hackathon requires a **working prototype** that addresses a chosen
problem statement. The solution must be functional and demonstrate the
idea in action, not merely present a pitch deck or static mockup.

## 1.2 Mandatory technology and deployment constraints

The supplied criteria state that submissions must:

-   Leverage Google AI models, such as Gemini or Gemma, **or** be built
    using qualifying agentic platforms such as Agent Platform,
    Antigravity, or AI Studio.
-   Be deployed on Google Cloud through **Cloud Run or Firebase**.
-   Demonstrate a working solution for the chosen problem statement.

The exact rules of the event should be checked again before submission,
especially any required services, judging rubric, eligibility rules, or
deployment restrictions.

## 1.3 Product implications

StoryPilot should be designed so that Google Cloud is part of the actual
working solution, rather than an incidental hosting label. A defensible
implementation uses Gemini through Vertex AI for language and reasoning
tasks, Cloud Run for the application/API, and Firestore or another
suitable store for canonical story records.

A local-only demonstration is insufficient if the submission criteria
require Google Cloud deployment. A production-grade enterprise
integration is not required for the initial MVP if the prototype
transparently uses representative data and demonstrates the workflow end
to end.

## 1.4 What a judge should be able to see

Within a short demonstration, a judge should be able to:

1.  Open an engineering story with incomplete or fragmented context.
2.  See StoryPilot retrieve and organize relevant evidence.
3.  See missing requirements or contradictions called out explicitly.
4.  Inspect source references supporting the findings.
5.  Approve or reject generated clarification questions or
    documentation.
6.  See the canonical story record update and produce a useful output.
7.  Understand the measurable benefit compared with a manual baseline.

------------------------------------------------------------------------

# 2. Theme Selection Analysis

Six themes were considered:

1.  BFSI: Intelligent Risk, Fraud & Financial Experiences.
2.  Retail & Commerce: Intelligent Customer and Business Experiences.
3.  Manufacturing: Intelligent Operations & Industrial Efficiency.
4.  Media, Content & Digital Experiences.
5.  Future of Work & Enterprise Productivity.
6.  Sustainability & Social Impact.

The strategy was to retain themes with a credible combination of impact,
differentiation, technical depth, and achievable demonstration, while
eliminating themes whose most obvious implementations risk being generic
or difficult to differentiate.

## 2.1 Comparative assessment

Scores below are subjective strategy ratings from 1 to 5. They are not
official competition scores. For "similar-project risk," a higher score
means greater risk that many teams will submit similar concepts.

  --------------------------------------------------------------------------------------------
  Theme                  Impact   Differentiation         Build     AI depth   Similar-project
                                        potential   feasibility                           risk
  ---------------- ------------ ----------------- ------------- ------------ -----------------
  BFSI                        5                 4             4            5                 4

  Retail &                    4                 2             5            4                 5
  Commerce                                                                   

  Manufacturing               5                 5             3            5                 2

  Media & Digital             3                 2             5            3                 5
  Experiences                                                                

  Future of Work &            4                 3             5            4                 5
  Enterprise                                                                 
  Productivity                                                               

  Sustainability &            5                 5             4            4                 3
  Social Impact                                                              
  --------------------------------------------------------------------------------------------

These numbers are meant to support discussion, not substitute for
checking the specific problem statement, judging rubric, dataset
availability, or deadline.

## 2.2 BFSI: Intelligent Risk, Fraud & Financial Experiences

### Potential problem statements

-   Detect suspicious transaction patterns and explain why they merit
    review.
-   Identify inconsistencies or missing evidence in insurance claims.
-   Help consumers understand loan terms, fees, and financial risk.
-   Identify likely social-engineering or payment scams before a victim
    transfers funds.

### Advantages

-   Financial fraud and consumer protection have clear real-world
    consequences.
-   Strong technical opportunities in anomaly detection, structured-data
    analysis, explainable decisions, and AI-assisted investigation.
-   A demo can show a suspicious case being identified, explained, and
    escalated.

### Disadvantages

-   Basic fraud classification is a common project idea.
-   Real financial data may be unavailable; synthetic data can weaken
    credibility if not clearly labeled.
-   False positives, fairness, privacy, and financial accuracy are
    important concerns.

### Strategic verdict

A strong contender if the team finds a specific underserved financial
problem rather than building a generic fraud classifier.

## 2.3 Retail & Commerce: Intelligent Customer and Business Experiences

### Potential problem statements

-   Predict stockouts and excess inventory for small retailers.
-   Forecast demand using sales history and seasonal patterns.
-   Detect suspicious returns or repeated refund abuse.
-   Help customers find products based on complex needs.

### Advantages

-   Sample data is relatively easy to create or source.
-   Business value can be measured through inventory waste, stockouts,
    and processing time.
-   A prototype is generally straightforward to deploy.

### Disadvantages

-   Shopping assistants, recommendations, and customer-support bots are
    common.
-   Personalization demos may look attractive without proving measurable
    value.
-   Differentiation often depends on realistic business data and
    integrations.

### Strategic verdict

Rejected from the initial shortlist as a primary theme because the most
obvious solutions are highly replicable. Retail ideas can still be
revisited if a distinct problem emerges.

## 2.4 Manufacturing: Intelligent Operations & Industrial Efficiency

### Potential problem statements

-   Predict machine failures from sensor readings.
-   Identify quality defects using images and inspection records.
-   Find energy waste and recommend efficient operating schedules.
-   Explain production bottlenecks using downtime, inventory, and
    maintenance records.

### Advantages

-   Specific operational failures can be expensive and measurable.
-   Opportunities for time-series analysis, computer vision,
    optimization, and language-model reasoning.
-   A prototype can show a warning, evidence, recommended intervention,
    and estimated savings.
-   Potentially strong differentiation from generic chatbot projects.

### Disadvantages

-   Credible industrial telemetry can be difficult to obtain.
-   Predictive claims require suitable data and validation.
-   A simulated factory dashboard with AI-generated recommendations
    alone would be unconvincing.

### Strategic verdict

Retained as a strong alternative because it offers technical depth and
an opportunity to solve a narrow, consequential problem.

## 2.5 Media, Content & Digital Experiences

### Potential problem statements

-   Make educational material accessible across languages and reading
    levels.
-   Detect misleading edits or inconsistencies in digital media.
-   Help users find trustworthy information in large content
    collections.
-   Generate accessible descriptions for multimedia.

### Advantages

-   Multimodal AI can work with text, audio, images, and video.
-   A polished prototype can be built quickly.
-   Accessibility and multilingual education can create meaningful
    impact.

### Disadvantages

-   Content generation, summarization, and chatbots are heavily
    replicated.
-   Content generation alone may not establish a distinctive impact.
-   Authenticity verification is difficult to demonstrate reliably
    without strong evidence.

### Strategic verdict

Rejected from the initial shortlist as a primary theme unless a specific
accessibility or information-integrity problem offers a stronger
opportunity.

## 2.6 Future of Work & Enterprise Productivity

### Potential problem statements

-   Retrieve answers from scattered policies, documents, and technical
    records with source citations.
-   Automate repetitive multi-step workflows with approval checkpoints.
-   Detect inconsistencies across procedures, tickets, and
    documentation.
-   Assist engineers in investigating incidents using logs, runbooks,
    and historical cases.
-   Reduce context-gathering and coordination overhead around software
    stories.

### Advantages

-   Strong fit for Gemini, retrieval-augmented generation (RAG), tool
    use, and agentic workflows.
-   A controlled dataset makes a functional prototype feasible.
-   Time saved, completeness, retrieval quality, and error reduction can
    be measured.
-   The team can build a practical end-to-end workflow rather than a
    pitch-only concept.

### Disadvantages

-   Generic enterprise assistants and document chatbots are common.
-   RAG alone is not a strong differentiator.
-   A system that only summarizes documents may look like a thin wrapper
    around a model.

### Strategic verdict

Chosen as the project theme because StoryPilot can address a specific
workflow problem within it. The project must be framed around verifiable
engineering outcomes, not generic productivity.

## 2.7 Sustainability & Social Impact

### Potential problem statements

-   Prioritize community reports about waste, water leaks, or
    environmental hazards.
-   Coordinate redistribution of food surplus before it becomes waste.
-   Help vulnerable users navigate public services and accessibility
    barriers.
-   Detect unusual water or energy consumption and recommend
    interventions.

### Advantages

-   Strong human impact when the target community and problem are well
    defined.
-   Opportunities for image understanding, forecasting, geospatial
    analysis, and agentic workflows.
-   Potential to demonstrate measurable outcomes such as reduced waste
    or response time.

### Disadvantages

-   Broad claims such as "use AI to save the planet" are too vague.
-   Impact estimates need evidence and should be labeled honestly.
-   Community coordination features need a reliable path from
    recommendation to action.

### Strategic verdict

Retained as a strong alternative because of its combination of societal
value, technical opportunity, and potentially distinctive problem
spaces.

## 2.8 Three themes initially removed

The initial shortlist removes:

1.  **Retail & Commerce** --- not because it is inherently weak, but
    because common recommendation and shopping-agent implementations are
    easy to replicate.
2.  **Media & Digital Experiences** --- generic generation and
    summarization projects have limited differentiation.
3.  **Future of Work as a broad, generic assistant theme** --- this is a
    narrowing decision, not a final rejection of the theme. StoryPilot
    later re-enters this theme as a narrowly scoped, evidence-driven
    engineering workflow.

This distinction matters: the general theme is not inherently
unsuitable. The team is choosing to avoid generic implementations within
it.

## 2.9 Retained themes

The three retained themes for initial strategic consideration were:

-   BFSI, for explainable financial risk and consumer protection.
-   Manufacturing, for measurable industrial efficiency.
-   Sustainability & Social Impact, for targeted community and
    environmental challenges.

StoryPilot was then selected as a preferred direction within Future of
Work because it aligns with the team's software engineering experience
and can be demonstrated with controlled data and a focused end-to-end
workflow.

------------------------------------------------------------------------

# 3. StoryPilot Product Concept

## 3.1 Working title

**StoryPilot: Evidence-Driven Software Story Intelligence**

Alternative tagline:

> An AI co-pilot that follows every story from assignment to
> documentation, so developers can spend less time chasing context,
> replies, and paperwork.

The pilot co-pilot analogy is useful: the developer remains responsible
for the implementation, while the assistant organizes context, surfaces
gaps, tracks evidence, prepares drafts, and maintains records.

## 3.2 Core problem

Software engineering teams lose time and introduce avoidable rework
because requirements, architectural context, implementation evidence,
decisions, and technical documentation are fragmented across work items,
repositories, pull requests, and knowledge bases.

Developers manually collect context, chase clarification, reconstruct
activity, and update documentation. Important details can be missed,
outdated information can be reused, and completion records may not
reflect the actual change.

## 3.3 Proposed solution

StoryPilot assembles an evidence-linked context brief for each
engineering story, identifies missing or contradictory requirements,
maps acceptance criteria to implementation evidence, and drafts
completion documentation from verified inputs.

The system uses a canonical story record to preserve relevant facts,
decisions, questions, source references, activity, and outputs
throughout the lifecycle. A human approval workflow ensures that
external communications and published artifacts remain under developer
control.

## 3.4 Core product principle: capture once, reuse everywhere

Every stage should update or derive from one story record. The same
record powers:

-   Context briefs.
-   Missing-information reports.
-   Clarification questions.
-   Decision records.
-   Requirements-to-evidence matrices.
-   Activity summaries.
-   Documentation drafts.
-   Optional timesheet drafts.
-   Readiness and risk summaries.

The system should not ask users to manually maintain the same
information in multiple outputs.

## 3.5 Proposed pitch

> **StoryPilot is an evidence-driven AI co-pilot for software
> engineering stories. It gathers scattered technical context, exposes
> missing requirements before coding, traces acceptance criteria to
> implementation evidence, and drafts trustworthy completion
> documentation---all from one canonical story record, with developers
> in control.**

## 3.6 Product differentiation

The project should not claim that multi-agent architecture alone makes
it original. The stronger differentiators are:

1.  **Evidence-linked outputs:** Important findings link back to the
    exact source, document excerpt, story field, or code-diff segment
    that supports them.
2.  **Explicit uncertainty:** The system distinguishes confirmed facts,
    inferred suggestions, missing information, and conflicting evidence.
3.  **Requirement traceability:** Acceptance criteria are mapped to
    evidence rather than merely summarized.
4.  **One canonical record:** Multiple lifecycle outputs reuse shared
    data.
5.  **Human approval:** Drafts are not silently sent or published.
6.  **Evaluation:** The prototype measures missing-gap detection,
    evidence support, completeness, and time to produce outputs.

------------------------------------------------------------------------

# 4. Full Lifecycle Vision

The full vision includes seven connected stages. They should be treated
as a product roadmap, not a requirement to implement every stage during
the hackathon.

## 4.1 Stage 1: Story assigned

Input may include:

-   Story identifier and title.
-   Description.
-   Acceptance criteria.
-   Priority and owner.
-   Linked issues.
-   Relevant documents.
-   Repository and code references.

Output: a canonical story record with a clear lifecycle status.

## 4.2 Stage 2: Context brief assembled

The context agent retrieves relevant technical information from a
controlled corpus and organizes it into:

-   What is known.
-   Relevant architecture and dependencies.
-   Existing implementation patterns.
-   Related past decisions or incidents.
-   Acceptance criteria.
-   Missing or conflicting information.
-   Sources supporting each important statement.

The brief should be concise enough to use before implementation and
detailed enough to reduce manual investigation.

## 4.3 Stage 3: Gaps identified and questions prepared

The clarification agent identifies ambiguities and missing requirements,
then generates focused questions.

Example categories:

-   Unspecified input validation.
-   Unclear behavior for an edge case.
-   Missing error-handling expectations.
-   Unclear authorization behavior.
-   Inconsistent documentation.
-   Missing acceptance tests.
-   Conflicting business rules.

Questions should be grouped and prioritized to avoid sending many
low-value messages.

A future integration could schedule a message according to the product
owner's time zone. For the MVP, a simulated scheduled-send state is
sufficient; no claim of real scheduling should be made unless it is
implemented.

The system should track:

-   Drafted question.
-   Approval status.
-   Sent status, if genuinely integrated.
-   Response.
-   Decision captured.
-   Brief updated.
-   Remaining unresolved questions.

## 4.4 Stage 4: Development activity captured

Potential sources include commits, pull requests, reviews, tickets, and
support records.

The activity agent should distinguish:

-   **Observed events:** supported by actual supplied records.
-   **Inferred activities:** possible work inferred from the data.
-   **User-entered activities:** explicitly provided by a developer.

Do not treat a commit timestamp as proof of the exact time spent
working. Do not infer billable hours from event counts.

For the MVP, use a supplied activity dataset or manually entered events.
A real GitHub integration can be added if time permits.

## 4.5 Stage 5: Pre-PR checks and evidence review

Potential future checks include:

-   Acceptance criteria without linked implementation or test evidence.
-   Changed behavior without a corresponding test.
-   Documentation likely to be outdated.
-   Unresolved requirements that affect correctness.
-   Existing security-scan findings that require triage.
-   Missing reviewer or approval requirements.

The MVP should focus on requirement traceability and evidence gaps.
Fortify triage and complex automated security analysis belong in the
roadmap unless a real tool integration and validation approach are
available.

A language model should not claim a change is secure merely because it
generated a reassuring summary.

## 4.6 Stage 6: Story completion and documentation

When a story is marked complete, the docs agent drafts documentation
based on:

-   Approved story requirements.
-   Confirmed decisions.
-   Supplied implementation diff.
-   Test evidence.
-   Known limitations.
-   Relevant existing documentation.

Outputs may include:

-   Summary of the change.
-   Behavior before and after.
-   API or configuration changes.
-   Validation and test results.
-   Operational notes.
-   Known limitations.
-   Related requirements and source references.

The agent must not invent endpoints, configuration values, test results,
or architectural facts.

## 4.7 Stage 7: Reporting and optional timesheet draft

The system can summarize:

-   Completed stories.
-   Outstanding questions.
-   Review blockers.
-   Documentation awaiting approval.
-   Risks to a target release.
-   Recorded activity.

A timesheet draft can be generated only from explicit user-entered
durations or trusted source records. If duration evidence is missing,
the system should mark it as unknown rather than fabricate it.

## 4.8 MVP stage selection

Recommended MVP:

-   Stage 1: story record.
-   Stage 2: context brief.
-   Stage 3: gap detection and clarification drafts.
-   Stage 5: limited requirements-to-evidence review.
-   Stage 6: documentation draft.
-   Approval queue and audit trail.

Stages 4 and 7 can use a small seeded activity dataset or be
demonstrated as secondary outputs. Broad live integrations and automated
pre-PR security triage should remain roadmap items.

------------------------------------------------------------------------

# 5. Candidate Problem Statements Within StoryPilot

The following statements are proposed concepts, not official
organizer-issued problem statements.

## P1. Context fragmentation and requirement gaps

**Problem statement:** Software developers receive work items whose
requirements, implementation history, architectural dependencies, and
acceptance criteria are distributed across multiple sources. This
fragmentation causes avoidable investigation, incorrect assumptions, and
rework.

**Solution:** Assemble an evidence-linked brief, identify missing
information, and generate clarification questions before coding starts.

**Demo:** Supply an incomplete story and several technical documents.
The system identifies missing requirements and cites supporting sources.

**Difficulty:** Medium.

**Strategic view:** Best central problem statement for the project.

## P2. Requirements-to-code traceability gaps

**Problem statement:** Teams struggle to establish whether
implementation changes and documentation actually satisfy a work item's
requirements and acceptance criteria.

**Solution:** Map requirements to evidence in design notes, code diffs,
tests, and documentation. Flag requirements without adequate evidence.

**Demo:** Upload a story, code diff, and test results. Generate a
traceability matrix with covered, uncovered, and uncertain requirements.

**Difficulty:** Medium to high.

**Strategic view:** Strongest verification capability to combine with
P1.

## P3. Delays caused by unresolved requirements

**Problem statement:** Ambiguous stories create repeated clarification
cycles, delay implementation, and cause decisions to be lost across
conversations.

**Solution:** Identify ambiguities, group related questions, prioritize
blockers, prepare a concise clarification request, and track answers
against the story.

**Demo:** Show an incomplete story, generated questions, a simulated
product-owner response, and an updated brief.

**Difficulty:** Low to medium.

**Strategic view:** Useful supporting workflow.

## P4. Documentation drift after code changes

**Problem statement:** Technical documentation becomes inconsistent with
implemented software because updating it requires a separate manual
effort after changes are made.

**Solution:** Compare a story, approved requirements, and a code diff;
draft documentation that identifies changes and links claims to
evidence.

**Demo:** Supply old documentation and a code diff. Show outdated
statements and proposed replacements.

**Difficulty:** Low to medium.

**Strategic view:** Strong visible output, but less distinctive when
implemented as documentation generation alone.

## P5. Hidden delivery risks and stale status updates

**Problem statement:** Project reports depend on manual updates and fail
to expose unresolved blockers, unanswered questions, or incomplete
acceptance criteria until late in delivery.

**Solution:** Derive a story readiness assessment from available
evidence and highlight blockers, missing information, and overdue
decisions.

**Demo:** Supply stories with different states and blockers. Generate a
risk report with evidence and suggested actions.

**Difficulty:** Medium.

**Strategic view:** Useful after the core evidence model exists.

## P6. Fragmented engineering activity records

**Problem statement:** Activity is spread across commits, pull requests,
reviews, tickets, and support conversations, making handovers, progress
reports, and end-of-cycle records tedious.

**Solution:** Aggregate activity into a story timeline, distinguish
observed events from inferred work, and draft summaries for human
approval.

**Demo:** Feed a small activity dataset and generate a chronological
log.

**Difficulty:** Low to medium.

**Strategic view:** Useful supporting capability, not the primary hero
feature.

------------------------------------------------------------------------

# 6. Additional Productivity Problem Statements

These concepts can be considered alternatives or future extensions. Each
is a proposed problem, not an assertion that the space is unserved or
that competitors do not exist.

## A. Decision Debt Detector

**Problem:** Decisions made in meetings, emails, and chat threads lose
their rationale, owner, or follow-up action.

**Solution:** Extract decisions, detect potentially conflicting or
superseded decisions, identify missing owners and deadlines, and produce
a source-linked decision register.

**MVP flow:** Import notes and messages → extract decisions → flag
conflicts → review and approve register.

**Differentiation:** Focuses on which decision is authoritative, not
merely on summarizing conversations.

**Risk:** Language may be ambiguous; inferred decisions need review.

## B. Incident Memory --- Stop Solving the Same Bug Twice

**Problem:** Teams repeatedly investigate failures whose causes and
fixes were already documented in old incidents, tickets, or postmortems.

**Solution:** Retrieve similar historical incidents, compare symptoms
and fixes, explain why a match is relevant, and generate a grounded
investigation checklist.

**MVP flow:** Load past incidents → submit a new error → retrieve
similar cases → show evidence and next steps.

**Differentiation:** Technical retrieval plus evidence-based
recommendations.

**Risk:** Similarity does not prove a common root cause; results must be
presented as candidates.

## C. Change Impact Navigator

**Problem:** Developers struggle to identify APIs, services, tests, and
documents potentially affected by a proposed code change.

**Solution:** Analyze a supplied diff and a repository map, then
identify candidate dependencies and tests that may need review.

**MVP flow:** Supply repository excerpt and diff → trace known
dependencies → show impact candidates with evidence.

**Differentiation:** Produces a concrete engineering artifact.

**Risk:** A small prototype cannot safely claim exhaustive dependency
discovery.

## D. Knowledge Contradiction Auditor

**Problem:** Internal documentation contains conflicting instructions,
outdated procedures, and duplicate policies.

**Solution:** Compare a curated document set, flag contradictory claims,
display sources and dates, and propose a correction for human approval.

**MVP flow:** Ingest documents → identify possible conflicts → explain
evidence → draft corrections.

**Differentiation:** Audits the reliability of the knowledge base
instead of merely answering questions.

**Risk:** Apparent contradictions may reflect different scopes or
versions.

## E. Handover Guardian

**Problem:** Leave or task-transfer handovers omit unresolved questions,
dependencies, and next actions.

**Solution:** Build a handover brief from task records, notes, and
recent activity, separating confirmed facts, pending decisions, owners,
and suggested next steps.

**MVP flow:** Supply task history → generate structured handover →
compare against a known checklist.

**Differentiation:** Highly practical and easy to validate.

**Risk:** May seem too narrow without a measurable evaluation.

## F. Meeting-to-Execution Agent

**Problem:** Meetings produce action items that do not reliably become
tracked, assigned work.

**Solution:** Extract actions, owners, and deadlines, detect missing
ownership, and prepare draft tasks for approval.

**MVP flow:** Notes → action extraction → ambiguity detection → approval
queue → task export.

**Differentiation:** Converts discussion into verified work items rather
than stopping at a summary.

**Risk:** Generic meeting assistants are common; workflow execution and
verification are essential.

## G. Policy-to-Action Navigator

**Problem:** Employees know a policy exists but cannot easily apply it
to a situation or determine the required approval.

**Solution:** Use a controlled policy set to identify applicable rules,
evidence, approvals, and next steps with source citations.

**MVP flow:** Policy collection → scenario input → cited checklist →
human review.

**Differentiation:** Actionable, source-grounded application of policy.

**Risk:** Incorrect interpretation could have consequences; the domain
should be chosen carefully.

## H. Workload Friction Analyzer

**Problem:** Repeated blockers, review delays, and handoffs consume team
capacity but are difficult to identify from fragmented activity data.

**Solution:** Analyze a supplied project activity dataset to surface
recurring bottlenecks and quantify where work waits.

**MVP flow:** Event dataset → bottleneck analysis → evidence-backed
recommendations → before/after simulation.

**Differentiation:** Operational insight beyond task counts.

**Risk:** The conclusions are only as reliable as the event data and
definitions.

------------------------------------------------------------------------

# 7. Candidate Ranking and Selection

Subjective ranking for a short hackathon build:

  ------------------------------------------------------------------------
                   Rank Concept          Main advantage   Main risk
  --------------------- ---------------- ---------------- ----------------
                      1 StoryPilot:      Coherent         Scope creep
                        context gaps +   end-to-end       
                        traceability     engineering      
                                         workflow         

                      2 Incident Memory  Clear technical  Can resemble
                                         demo and         standard RAG
                                         measurable       
                                         retrieval        
                                         quality          

                      3 Decision Debt    Distinct         Ambiguous
                        Detector         workplace        decision
                                         problem          extraction

                      4 Change Impact    Strong           Dependency
                        Navigator        engineering      analysis must be
                                         depth            credible

                      5 Knowledge        Audits the       False conflict
                        Contradiction    source knowledge detection
                        Auditor          itself           

                      6 Handover         Fast and         May seem too
                        Guardian         practical        small without
                                                          evaluation
  ------------------------------------------------------------------------

The recommended project is **StoryPilot**, with context analysis as the
core and traceability as its verification capability. Documentation
generation is the final visible output. Clarification is a supporting
workflow.

------------------------------------------------------------------------

# 8. Functional Requirements

## 8.1 Core requirements

### FR-1: Create and load a story

The user can create a story or load a supplied sample. The story has an
identifier, title, description, acceptance criteria, status, priority,
and source references.

### FR-2: Ingest supporting context

The user can attach or select relevant technical documents, code
excerpts, change diffs, test evidence, and existing documentation.

The prototype should clearly indicate which materials were actually
loaded. It must not imply it connected to a real Jira, Confluence,
GitHub, or email account unless that integration is working.

### FR-3: Generate a context brief

The system produces:

-   Summary of the requested change.
-   Relevant architecture or implementation context.
-   Known facts.
-   Missing information.
-   Potential contradictions.
-   Suggested next steps.
-   Source references for material claims.

### FR-4: Detect requirement gaps

The system evaluates the story and available sources for ambiguous,
missing, or conflicting requirements.

Each finding should contain:

-   Stable finding identifier.
-   Description.
-   Severity or priority.
-   Supporting evidence.
-   Why the evidence indicates a gap.
-   Suggested clarification question.
-   Confidence or uncertainty label.
-   Review status.

### FR-5: Generate clarification questions

The system creates concise, grouped questions. Questions should be
phrased to resolve an identifiable ambiguity and avoid asking the user
to restate information already present in the sources.

### FR-6: Build a traceability matrix

Each acceptance criterion is mapped to evidence, such as a code diff,
test result, or design document. The system labels coverage as:

-   Supported by supplied evidence.
-   No supporting evidence found.
-   Conflicting evidence.
-   Not enough information to determine.

"No evidence found" must not automatically mean "implementation is
missing." The scope of supplied data should be visible.

### FR-7: Generate completion documentation

The system drafts documentation from approved facts, accepted decisions,
and supplied implementation evidence. Unsupported facts should be marked
as unknown or left out.

### FR-8: Approval queue

Every generated external-facing artifact has a state:

-   Draft.
-   Awaiting review.
-   Approved.
-   Rejected.
-   Published/exported, if the action actually occurred.

The prototype should not claim publication or delivery merely because a
draft was approved.

### FR-9: Audit trail

Record meaningful events, including analysis requests, findings
generated, user decisions, revisions, approvals, and exports.

### FR-10: Demonstrate evaluation

The system includes a repeatable test dataset and displays evaluation
results for gap detection, evidence support, completeness, and workflow
time.

## 8.2 Secondary requirements

-   Generate a chronological story activity summary.
-   Prepare a release-readiness summary.
-   Draft a timesheet from explicit durations only.
-   Simulate clarification follow-up.
-   Export generated documentation as Markdown.
-   Provide a way to inspect sources used for each important finding.

## 8.3 Explicitly out of scope for the initial MVP

-   Full real-time integrations with every enterprise tool.
-   Automatic messages to product owners without approval.
-   Automatic publishing to Confluence without approval.
-   Production-grade repository-wide dependency analysis.
-   Full security scanning or replacement for Fortify.
-   Automatic timesheet submission.
-   Claims of complete coverage from partial repository context.
-   Complex multi-tenant enterprise identity and permission management
    unless required.

------------------------------------------------------------------------

# 9. Non-Functional Requirements and Trust

## 9.1 Grounded outputs

The model should only make factual claims supported by the supplied
evidence or clearly label them as hypotheses. Every important finding
should be traceable to source material.

## 9.2 Human oversight

The system drafts; the developer approves. No external communication,
ticket creation, or publication should occur without an explicit
approved action in the MVP.

## 9.3 Reproducibility

Given the same input data and prompt configuration, the system should
produce outputs that can be evaluated against a known test set. Model
output may vary, so test scoring should not depend on exact wording.

## 9.4 Privacy and data minimization

Use fabricated demo data or data the team is authorized to process.
Avoid uploading proprietary source code, customer data, credentials,
access tokens, or confidential production records to a public
demonstration.

## 9.5 Error handling

The application should handle missing files, malformed data, model
failures, unavailable services, and invalid user actions without
corrupting the canonical story record.

## 9.6 Transparent limitations

The interface should identify whether a result came from:

-   A real connected source.
-   A supplied file.
-   Seeded demo data.
-   An inference.
-   A user-entered value.

------------------------------------------------------------------------

# 10. Architecture and Technology Stack

## 10.1 Recommended logical architecture

``` text
Web UI
  |
  v
Application API on Cloud Run
  |
  +--> Story service ----------------------> Firestore
  |
  +--> Source ingestion and indexing
  |       |
  |       +--> Supplied files / demo corpus
  |       +--> Optional Vertex AI Search
  |
  +--> Gemini analysis service
  |       |
  |       +--> Context brief
  |       +--> Gap and contradiction detection
  |       +--> Clarification drafts
  |       +--> Traceability analysis
  |       +--> Documentation drafts
  |
  +--> Deterministic validation layer
  |       |
  |       +--> Required-field checks
  |       +--> Evidence-reference validation
  |       +--> Coverage calculations
  |       +--> Workflow-state validation
  |
  +--> Approval and audit service
          |
          +--> Firestore
          +--> Markdown export
```

## 10.2 Architecture principle

Do not make every capability a separate autonomous agent just because an
agent framework is available. Start with a small number of explicit,
testable workflow steps. Add agents only when tool use, state
transitions, or multi-step planning meaningfully improve the solution.

A single orchestrated workflow with specialized functions may be easier
to debug and evaluate than four independent agents communicating without
strict contracts.

## 10.3 Proposed technology stack

  -----------------------------------------------------------------------
  Layer                   Proposed technology     Reason
  ----------------------- ----------------------- -----------------------
  AI model                Gemini through Vertex   Reasoning, extraction,
                          AI                      synthesis, and
                                                  structured outputs

  Agent orchestration     Google ADK, if useful   Explicit multi-step
                                                  workflow and tool
                                                  calling

  Backend/API             Python with FastAPI, or Practical integration
                          a stack the team can    with AI libraries
                          deliver reliably        

  UI                      React, or a simple      Story page, evidence
                          server-rendered         viewer, approval queue
                          interface               

  Hosting                 Cloud Run               Meets stated Google
                                                  Cloud deployment route

  Canonical record        Firestore               Flexible story records
                                                  and event history

  Retrieval               Local/in-memory         Keep the first
                          retrieval for earliest  implementation
                          prototype; optional     manageable
                          Vertex AI Search        

  Source files            Controlled upload or    Avoid premature
                          packaged demo corpus    connector complexity

  Export                  Markdown                Easy to inspect and
                                                  demonstrate

  Analytics               Simple evaluation       Avoid unnecessary
                          report initially;       infrastructure
                          BigQuery later if       
                          needed                  
  -----------------------------------------------------------------------

## 10.4 Google Cloud service decisions

### Gemini / Vertex AI

Use for:

-   Extracting structured information from stories and documents.
-   Identifying ambiguity and possible conflicts.
-   Drafting focused clarification questions.
-   Summarizing supplied code diffs.
-   Drafting documentation.

Use structured output schemas where supported. Validate model responses
before persisting them.

### Google ADK

Use if the implementation benefits from explicit tools and a controlled
multi-step workflow. For example:

1.  Retrieve relevant sources.
2.  Extract known requirements.
3.  Compare them against acceptance criteria.
4.  Generate candidate findings.
5.  Validate references.
6.  Draft the final brief.

The orchestration should preserve step outputs and errors so the team
can debug the demo.

### Firestore

Store the canonical story record, source metadata, findings, questions,
decisions, generated artifacts, approvals, and audit events.

Keep large source files outside the story document if size or access
patterns make that appropriate. Store metadata and references rather
than repeatedly embedding large documents.

### Vertex AI Search

Consider it if there is enough time to set up a meaningful document
corpus and show useful retrieval. It should not be a prerequisite for
the first working vertical slice.

### Cloud Run

Deploy the UI/API in a way that is reliable for judges to access. Use
environment configuration and Secret Manager or an appropriate secure
configuration mechanism for credentials. Do not commit secrets to the
repository.

### BigQuery

Defer until the project has useful analytics needs. It is not necessary
to demonstrate the core value proposition.

### Agent Engine

Defer unless the final design genuinely needs its deployment or runtime
capabilities. The presence of multiple agents is not, by itself, a
reason to introduce another service.

## 10.5 Real connectors versus mock adapters

The connector layer should use an explicit interface, so the core
workflow can accept either a real source or a demo fixture.

Example conceptual interface:

``` python
class StorySource:
    def get_story(self, story_id: str) -> dict:
        raise NotImplementedError

    def get_context_documents(self, story_id: str) -> list[dict]:
        raise NotImplementedError

    def get_change_evidence(self, story_id: str) -> list[dict]:
        raise NotImplementedError
```

Implement a `DemoStorySource` first. A later adapter can implement Jira,
Confluence, GitHub, or Azure DevOps access. The UI must clearly label
the source mode.

------------------------------------------------------------------------

# 11. Canonical Story Data Model

The canonical record is the core of "capture once, reuse everywhere."

A simplified conceptual model:

``` json
{
  "story_id": "STORY-101",
  "title": "Validate payment request fields",
  "description": "Reject invalid requests before processing.",
  "status": "in_analysis",
  "priority": "high",
  "acceptance_criteria": [
    {
      "id": "AC-1",
      "text": "Missing account identifiers are rejected"
    },
    {
      "id": "AC-2",
      "text": "Invalid requests return the documented error response"
    }
  ],
  "sources": [
    {
      "source_id": "SRC-1",
      "type": "document",
      "name": "Payment API Guidelines",
      "location": "demo://docs/payment-api-guidelines.md"
    }
  ],
  "known_facts": [],
  "findings": [],
  "questions": [],
  "decisions": [],
  "implementation_evidence": [],
  "documentation_drafts": [],
  "activity_events": [],
  "audit_events": [],
  "created_at": "ISO-8601 timestamp",
  "updated_at": "ISO-8601 timestamp"
}
```

This is a conceptual example, not a complete production schema.

## 11.1 Data-model rules

-   Give each source, finding, question, criterion, decision, and
    artifact a stable ID.
-   Store the source location and a useful excerpt or locator for every
    evidence-backed claim.
-   Keep generated suggestions separate from confirmed facts.
-   Preserve approval status and revision history.
-   Do not silently overwrite approved decisions.
-   Track timestamps consistently.
-   Avoid storing secrets or unnecessary personal data.

## 11.2 Suggested finding structure

``` json
{
  "finding_id": "FIND-001",
  "category": "missing_requirement",
  "severity": "high",
  "statement": "The expected response for an expired token is not specified.",
  "evidence": [
    {
      "source_id": "SRC-1",
      "locator": "Authentication section",
      "excerpt": "Requests must include a valid access token."
    }
  ],
  "reasoning_summary": "The source requires a valid token but does not define the response for an expired token.",
  "suggested_question": "What response should the API return when the access token has expired?",
  "confidence": "medium",
  "review_status": "pending"
}
```

The excerpt and reasoning are illustrative. In a real implementation,
evidence must come from the actual supplied corpus.

------------------------------------------------------------------------

# 12. Agent and Workflow Design

## 12.1 Recommended workflow

Rather than building four loosely coupled autonomous agents immediately,
implement a controlled workflow with clearly defined stages.

### Step 1: Ingest

-   Validate the story input.
-   Assign or confirm IDs.
-   Load supporting documents and change evidence.
-   Normalize source metadata.
-   Record which data was supplied.

### Step 2: Retrieve

-   Select documents relevant to the story and its acceptance criteria.
-   Preserve source IDs, titles, locations, and excerpts.
-   Avoid feeding every available document to the model if retrieval can
    narrow the context.

### Step 3: Extract known facts

-   Extract requirements, constraints, APIs, dependencies, decisions,
    and test expectations.
-   Keep extracted facts linked to their sources.
-   Record conflicts rather than silently choosing one source.

### Step 4: Analyze gaps

-   Compare the story description and acceptance criteria with the
    retrieved evidence.
-   Generate candidate missing requirements and contradictions.
-   Require evidence for each finding.
-   Use deterministic validation to ensure evidence references exist.

### Step 5: Generate questions

-   Group duplicate questions.
-   Prioritize blockers.
-   Avoid asking about facts already established in the source set.
-   Create drafts for review.

### Step 6: Trace implementation evidence

-   Compare acceptance criteria with supplied diffs, tests, and design
    evidence.
-   Mark criteria as supported, unsupported by supplied evidence,
    conflicting, or unknown.
-   Do not claim complete code coverage.

### Step 7: Draft documentation

-   Use approved facts, decisions, and implementation evidence.
-   Include unresolved questions and limitations where relevant.
-   Avoid generating claims about tests that were not supplied.

### Step 8: Validate and persist

-   Validate output schema.
-   Check source references.
-   Persist findings and artifacts.
-   Add an audit event.
-   Update the UI.

## 12.2 Why this approach is preferable

It creates a reliable demonstration path, keeps model behavior
inspectable, and limits debugging to a small number of stages. It also
allows the team to add a more sophisticated ADK agent workflow later
without changing the core story model.

## 12.3 Human approval rules

Require approval before:

-   Sending a clarification request.
-   Creating or updating an external ticket.
-   Publishing documentation.
-   Marking a generated decision as confirmed.
-   Exporting a timesheet as final.

The MVP can use a simulated approval state for demo data, but must not
imply an external action occurred unless it did.

------------------------------------------------------------------------

# 13. UI and Demonstration Design

## 13.1 Screen 1: Today view

Display:

-   Stories requiring analysis.
-   Stories with unanswered questions.
-   Documentation awaiting approval.
-   Outstanding blockers.
-   Recent story activity.
-   A small release-readiness summary, if supported by the demo data.

Avoid a dashboard filled with decorative charts that do not support a
decision.

## 13.2 Screen 2: Story page

Recommended layout:

1.  Story title and current state.
2.  Description and acceptance criteria.
3.  Context brief.
4.  Source evidence.
5.  Missing requirements and contradictions.
6.  Clarification questions.
7.  Implementation traceability matrix.
8.  Documentation draft.
9.  Activity and audit history.

## 13.3 Screen 3: Approval queue

Each item should show:

-   Artifact type.
-   Proposed content.
-   Supporting evidence.
-   Unresolved uncertainty.
-   Approve and reject actions.
-   Resulting status.

Approval should update the canonical record and audit history.

## 13.4 Screen 4: Evaluation view

Show a compact set of measured outcomes:

-   Seeded gaps versus detected gaps.
-   Evidence references that pass validation.
-   Traceability coverage.
-   Unsupported claim count.
-   Documentation completeness.
-   Time to produce the output.

This can be more persuasive than a generic analytics dashboard.

------------------------------------------------------------------------

# 14. Implementation Roadmap

The deadline is not yet known, so this is a phase-based plan rather than
a promise of completion by a particular date.

## Phase 0: Scope and setup

**Deliverables**

-   Confirm final hackathon rules and submission deadline.
-   Choose the one primary demo journey.
-   Decide the source mode: demo fixtures, imported files, or one real
    integration.
-   Create the Google Cloud project and verify access to the chosen
    Gemini model.
-   Confirm deployment permissions and billing constraints.
-   Prepare three realistic test stories.

**Exit criterion:** The team can make a successful model call and deploy
a minimal service to the required platform.

## Phase 1: Data model and seed data

**Tasks**

-   Define story, source, finding, question, decision, evidence,
    artifact, and audit schemas.
-   Create a small, internally consistent sample corpus.
-   Include incomplete requirements and contradictory documents
    deliberately.
-   Create deterministic test expectations for each story.

**Exit criterion:** A story can be loaded, displayed, and persisted
without AI.

## Phase 2: Context brief

**Tasks**

-   Implement source ingestion.
-   Implement retrieval over the sample corpus.
-   Generate a structured context brief.
-   Validate the output schema.
-   Display source references and uncertainty.
-   Persist the result.

**Exit criterion:** A user can enter a story and receive a useful,
evidence-linked brief.

## Phase 3: Gap detection and clarification

**Tasks**

-   Compare acceptance criteria against supplied evidence.
-   Generate candidate gaps and contradictions.
-   Validate that evidence references exist.
-   Generate grouped clarification questions.
-   Add approval and rejection.
-   Persist decisions and revisions.

**Exit criterion:** The incomplete sample story produces expected gap
findings, and the user can approve or reject the questions.

## Phase 4: Traceability and documentation

**Tasks**

-   Load a sample code diff and test evidence.
-   Map criteria to evidence.
-   Display supported, unsupported, conflicting, and unknown states.
-   Draft completion documentation from approved information.
-   Export the documentation as Markdown.

**Exit criterion:** A judge can follow a requirement from the story to
its evidence and into the final draft.

## Phase 5: Cloud deployment and reliability

**Tasks**

-   Deploy the application to Cloud Run or the selected permitted Google
    Cloud route.
-   Configure secrets securely.
-   Verify the public demo URL.
-   Test invalid inputs and model errors.
-   Ensure the app does not lose data during normal workflow use.
-   Test from a clean browser session.

**Exit criterion:** The core demonstration works on the deployed
version, not only on a developer's laptop.

## Phase 6: Evaluation and presentation

**Tasks**

-   Run the fixed evaluation dataset.
-   Record results honestly.
-   Compare with a manual baseline.
-   Prepare a short demonstration sequence.
-   Document limitations and future work.
-   Prepare a fallback dataset in case an integration fails.

**Exit criterion:** The team can repeat the demo and explain how value
was measured.

------------------------------------------------------------------------

# 15. Prioritization Under a Tight Deadline

If time is limited, follow this order:

1.  A working deployed application.
2.  A story input and canonical record.
3.  A context brief with real source references.
4.  Gap detection on at least one intentionally incomplete story.
5.  An approval queue.
6.  Traceability matrix.
7.  Documentation export.
8.  Evaluation results.
9.  One real integration, only if it does not threaten the above.
10. Activity capture, timesheets, Fortify, and advanced release
    analytics later.

The critical path is not "build all the agents." It is **one complete,
reliable user journey**.

## Minimum viable demonstration

A viable first demo should support:

-   Loading one story.
-   Loading three to five relevant context sources.
-   Generating a context brief.
-   Detecting at least one seeded missing requirement.
-   Showing the evidence supporting the finding.
-   Drafting a clarification question.
-   Producing a traceability matrix.
-   Generating a documentation draft.
-   Approving or rejecting an artifact.
-   Persisting the state and showing the result on the deployed app.

------------------------------------------------------------------------

# 16. Evaluation Framework

A convincing prototype should be evaluated against predefined examples
rather than judged only by how impressive the generated text looks.

## 16.1 Build a small gold-standard dataset

Prepare at least three stories:

### Story A: Well-defined

-   Requirements are clear.
-   Supporting documents agree.
-   Relevant code and tests are supplied.
-   Expected result: few or no major gap findings.

### Story B: Incomplete

-   At least two acceptance criteria omit important behavior.
-   One source is insufficient to answer the missing question.
-   Expected result: the system detects the seeded gaps and asks
    targeted questions.

### Story C: Contradictory

-   Two documents specify different behavior.
-   Their versions or dates are visible.
-   Expected result: the system flags the conflict instead of silently
    choosing an answer.

A larger set of cases improves confidence if time permits.

## 16.2 Suggested metrics

### Gap detection recall

Of all known seeded gaps, how many did the system detect?

\[ `\text{Recall}`{=tex} = `\frac{\text{True positive gaps}}`{=tex}
{`\text{True positive gaps}`{=tex}+`\text{Missed gaps}`{=tex}} \]

### Gap detection precision

Of all flagged gaps, how many were genuine gaps?

\[ `\text{Precision}`{=tex} = `\frac{\text{True positive gaps}}`{=tex}
{`\text{True positive gaps}`{=tex}+`\text{False positive gaps}`{=tex}}
\]

### Evidence validity

Percentage of generated evidence references that resolve to actual
supplied sources and relevant excerpts.

### Claim support rate

Percentage of sampled factual claims in the brief and documentation that
are supported by supplied evidence.

### Traceability completeness

Percentage of acceptance criteria for which the system produces an
appropriate status and evidence assessment. This measures completion of
the assessment, not proof that the implementation is correct.

### Documentation completeness

Use a predefined checklist---for example, change summary, affected
behavior, validation evidence, limitations, and relevant
requirements---and score the output against it.

### Time saved

Compare the time required to produce a brief and documentation manually
with the time required using StoryPilot. Use the same test stories and a
consistent procedure. Report the actual measured result, not a
fabricated percentage.

## 16.3 Evaluation safeguards

-   Count false positives as well as missed findings.
-   Treat "no evidence supplied" differently from "requirement not
    implemented."
-   Keep the evaluation stories separate from prompt tuning examples
    where practical.
-   Do not report performance on a tiny synthetic dataset as proof of
    enterprise-scale effectiveness.
-   Label all synthetic data and simulation assumptions.
-   Include at least one case where the system should say it cannot
    determine the answer.

------------------------------------------------------------------------

# 17. Security, Privacy, and Reliability

## 17.1 Secrets and access

-   Never commit API keys, service-account credentials, or access
    tokens.
-   Use an appropriate secure secret-management mechanism for
    deployment.
-   Request only the minimum permissions required by any connector.
-   Keep demo data separate from real corporate data.

## 17.2 Source permissions

A future real connector should not let the model expose documents that
the user is not authorized to access. Retrieval must respect source
permissions where applicable.

## 17.3 Prompt injection in source documents

Treat retrieved documents and code comments as untrusted input. A source
document may contain instructions that attempt to override the intended
task. The workflow should treat such content as data, not as system
instructions, and should validate any tool actions separately.

## 17.4 Output validation

Use schema validation, source-reference checks, and deterministic
workflow rules. Do not trust a model-generated JSON object simply
because it parses.

## 17.5 Auditability

Log the source inputs, model task, generated artifact version, user
decision, and any external action that actually occurred. Avoid logging
secrets or unnecessary sensitive content.

## 17.6 Reliability

-   Provide clear errors for unavailable model or database services.
-   Preserve the last valid story record if a generation step fails.
-   Make generation steps repeatable where possible.
-   Avoid duplicate records when a request is retried.
-   Ensure the approval queue accurately reflects the current artifact
    version.

------------------------------------------------------------------------

# 18. Risks and Mitigations

  -----------------------------------------------------------------------
  Risk                    Consequence             Mitigation
  ----------------------- ----------------------- -----------------------
  Scope creep             No end-to-end workflow  Restrict MVP to
                          completed               context, gaps,
                                                  traceability, and docs

  Generic AI wrapper      Weak differentiation    Evidence-linked outputs
                                                  and measurable
                                                  validation

  Hallucinated            Incorrect engineering   Source citations,
  requirements            decisions               explicit uncertainty,
                                                  schema validation

  False gap findings      Reduced user trust      Gold-standard tests,
                                                  precision measurement,
                                                  human review

  Missing source data     Incomplete or           Label data coverage and
                          misleading analysis     avoid completeness
                                                  claims

  Integration delays      Demo fails near         Demo adapters and local
                          deadline                fixtures behind a
                                                  stable interface

  Model latency or quota  Slow or unavailable     Cache seeded outputs
  issues                  demo                    where appropriate;
                                                  provide clear fallback
                                                  behavior

  Cloud deployment issues Judges cannot access    Deploy early and test
                          the app                 the deployed
                                                  environment repeatedly

  Privacy concerns        Exposure of             Use fabricated or
                          confidential code or    authorized data and
                          documents               secure credentials

  Misleading timesheets   Incorrect work records  Require explicit
                                                  durations and approval

  Overengineered agents   Hard-to-debug           Start with a
                          orchestration           deterministic workflow
                                                  and add agents only
                                                  when needed

  Weak impact evidence    Claims sound            Measure against a
                          speculative             manual baseline and
                                                  publish limitations
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 19. Demo Script

Target length: approximately three minutes, adjustable to the event's
rules.

## Scene 1: The problem

Open a sample story with an unclear requirement and scattered technical
context.

Explain that a developer normally has to search multiple sources and
message colleagues before understanding what needs to be built.

## Scene 2: Context brief

Click "Analyze story."

Show the brief, relevant architecture information, and the source
references. Point out that the system distinguishes known facts from
missing information.

## Scene 3: Gap detection

Show a deliberately omitted acceptance criterion. StoryPilot flags it
and explains which sources were checked and why the behavior remains
unclear.

## Scene 4: Clarification approval

Show the generated question. Approve it or reject it. If the prototype
uses simulated communication, label the action as simulated and show the
state change.

## Scene 5: Traceability

Provide a sample code diff and test evidence. Show which acceptance
criteria have supporting evidence and which remain unverified.

## Scene 6: Documentation

Generate a documentation draft. Show that it reuses approved facts and
includes the relevant evidence.

## Scene 7: Proof

Show the evaluation view: seeded gaps detected, source references
validated, documentation checklist results, and measured task time.

**Closing message:** StoryPilot does not replace the developer. It
reduces the work needed to understand a story, identify uncertainty,
preserve evidence, and produce reliable completion records.

------------------------------------------------------------------------

# 20. Proposed Final Problem Statement

## StoryPilot: Evidence-Driven Software Story Intelligence

Software engineering teams lose time and introduce avoidable rework
because requirements, architectural context, implementation evidence,
and technical documentation are fragmented across work items,
repositories, and knowledge bases. Existing workflows require developers
to manually collect context, chase clarification, and maintain
documentation, while important details can be missed or become outdated.

StoryPilot is a Google Cloud-based AI co-pilot that assembles an
evidence-linked brief for each engineering story, identifies missing or
contradictory requirements, maps acceptance criteria to implementation
evidence, and generates documentation drafts from verified information.
A human approval workflow ensures that external communications and
published artifacts remain under developer control.

The project aims to reduce context-gathering effort, expose requirement
gaps earlier, and improve traceability from assignment to completion.

## 20.1 Short version for a submission form

StoryPilot uses Google AI to turn fragmented engineering context into
evidence-linked story briefs, detect requirement gaps, trace acceptance
criteria to implementation evidence, and draft trustworthy technical
documentation---with developers approving every important action.

------------------------------------------------------------------------

# 21. Implementation Checklist

Use this checklist as the working execution plan.

## Scope and setup

-   [ ] Confirm deadline and judging rubric.
-   [ ] Confirm permitted Google Cloud services and AI model access.
-   [ ] Choose the primary demo story and user journey.
-   [ ] Prepare three labeled sample stories.
-   [ ] Create a canonical data model.
-   [ ] Decide between fixtures, imported files, and a real connector.

## Core workflow

-   [ ] Story creation/loading.
-   [ ] Source ingestion.
-   [ ] Retrieval and context brief.
-   [ ] Evidence-linked gap detection.
-   [ ] Clarification question drafts.
-   [ ] Human approval queue.
-   [ ] Requirements-to-evidence matrix.
-   [ ] Documentation draft and Markdown export.
-   [ ] Audit trail.

## Quality and trust

-   [ ] Validate structured model outputs.
-   [ ] Validate source references.
-   [ ] Display uncertainty and missing evidence.
-   [ ] Test incomplete and contradictory examples.
-   [ ] Measure precision and recall for seeded gaps.
-   [ ] Measure documentation completeness.
-   [ ] Compare task time with a manual baseline.
-   [ ] Avoid unsupported impact claims.

## Deployment

-   [ ] Configure secure credentials.
-   [ ] Deploy to Cloud Run or another permitted target.
-   [ ] Verify the deployed URL.
-   [ ] Test from a clean browser session.
-   [ ] Test failure states.
-   [ ] Confirm that the deployed version has the same behavior as the
    demo environment.
-   [ ] Prepare a fallback plan for any external integration.

## Presentation

-   [ ] Prepare a repeatable three-minute demo.
-   [ ] Show the problem before the solution.
-   [ ] Demonstrate evidence-linked findings.
-   [ ] Demonstrate a human approval action.
-   [ ] Show traceability and generated documentation.
-   [ ] Show actual evaluation results.
-   [ ] Explain limitations honestly.
-   [ ] Keep advanced features clearly labeled as roadmap items.

------------------------------------------------------------------------

# 22. Final Recommendation

StoryPilot is a promising direction for the Future of Work & Enterprise
Productivity theme, provided it is positioned as **evidence-driven
software story intelligence**, not simply an AI productivity assistant.

The recommended build is a focused vertical slice:

1.  Ingest a story and a small set of technical sources.
2.  Produce a source-linked context brief.
3.  Detect missing or contradictory requirements.
4.  Map acceptance criteria to supplied implementation evidence.
5.  Draft completion documentation from approved information.
6.  Preserve human approval and an audit trail.
7.  Deploy the working prototype on Google Cloud and evaluate it on a
    repeatable test set.

Do not build the entire seven-stage lifecycle before proving the core
workflow. Start with a coherent end-to-end path, demonstrate measurable
value, and add integrations only when they strengthen the proof rather
than threaten delivery.

The strongest promise is simple:

**StoryPilot helps developers move from a fragmented, ambiguous story to
an evidence-backed, documentation-ready change---without asking them to
trust an opaque AI answer.**

------------------------------------------------------------------------

# Appendix A. Assumptions and Open Decisions

The following details must be confirmed before implementation:

1.  Exact submission deadline.
2.  Official judging rubric and weighting.
3.  Team size and available development hours.
4.  Whether Google Cloud billing and model access are available.
5.  Which services are permitted or encouraged by the event.
6.  Whether real Jira, Confluence, GitHub, or Azure DevOps access is
    available.
7.  Whether the team can use authorized work data or must use fabricated
    data.
8.  Whether a public deployed URL is required.
9.  Whether the event expects a live connector or accepts a transparent
    demonstration corpus.
10. Whether any restrictions apply to third-party libraries, model
    calls, or data storage.

# Appendix B. Glossary

-   **Acceptance criteria:** Conditions that define what a story must
    satisfy.
-   **Agent:** A model-driven component that can perform a task and,
    where configured, use tools within defined limits.
-   **Canonical story record:** The authoritative application record for
    the story and its associated evidence and outputs.
-   **Evidence-linked output:** A generated statement or finding that
    references the source material supporting it.
-   **Firestore:** Google Cloud's document-oriented database service.
-   **Gemini:** Google's family of AI models.
-   **Google ADK:** Agent Development Kit for building agentic
    applications.
-   **Human-in-the-loop:** A workflow in which a person reviews or
    approves important decisions or actions.
-   **RAG:** Retrieval-augmented generation; retrieving relevant source
    material before generating a response.
-   **Traceability matrix:** A mapping between requirements and evidence
    such as design, implementation, tests, or documentation.
-   **Cloud Run:** Google Cloud's managed platform for running
    containerized applications.
-   **Vertex AI Search:** A Google Cloud search and retrieval service
    that can support retrieval across indexed content.

# Appendix C. Source and Claim Notes

This report is based primarily on the problem statements, project
concept, and hackathon criteria provided in the planning conversation.
Ratings and rankings are strategic judgments for planning, not verified
competition results. The proposed implementation architecture is a
recommendation and must be checked against the current Google Cloud
documentation, project permissions, and final hackathon rules before
execution.

No claim is made that StoryPilot has been implemented, benchmarked,
deployed, or validated in a real engineering organization.
