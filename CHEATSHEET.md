# LLD Cheat Sheet

> My personal LLD interview prep reference. Source: Hello Interview LLD docs.
> This is a LIVING doc — I add patterns & lessons as I learn them.

---

## The Delivery Framework (run this on EVERY problem)

| # | Step | What it means | Output |
|---|------|---------------|--------|
| 1 | **Requirements** | Functional verbs ("user can X") + non-functional (scale, concurrency, constraints). Ask clarifying questions. | Short bullet list |
| 2 | **Entities** | The nouns. Pull them straight from requirements. Just name them, don't design yet. | List of core objects |
| 3 | **Classes** | Give each entity shape: attributes + public methods + relationships (has-a / is-a). | Rough class diagram / skeleton |
| 4 | **Implementation** | Code the bodies of the KEY methods (the core flow). Not everything. | Working core logic |
| 5 | **Extensibility** | "What if requirements change?" New feature = new class, not edited old one (OCP). This is where patterns earn their place. | Design that bends, not breaks |

**Mantra:** Steps 1–3 are mechanical (extract nouns → shape them). The judgment is in 4 & 5.

---

## How I Practice (coaching rules — Claude, follow these)

1. I try the problem **myself, 3–4 attempts**, forcing my brain. NO answers from Claude.
2. Claude gives **hints only**, never the solution.
3. After my attempt, Claude tells me:
   - What requirements I **missed**
   - What entities/classes I **missed or got wrong**
   - How the design could be **modified / extended**
4. Goal = **unlock the method** so any new problem feels like the same 5 steps.

---

## Design Patterns (filling in as I learn)

> For each: what problem it solves + the one-line "when to reach for it".

| Pattern | Solves | Reach for it when... |
|---------|--------|----------------------|
| Strategy | swap an algorithm at runtime | many ways to do one thing (fees, pricing, sorting) |
| Factory | centralize object creation | creation logic is complex / type decided at runtime |
| Singleton | one shared instance | exactly one of something (config, connection pool) |
| _..._ | | |

---

## Problems Practiced (log)

| Problem | Attempts | Key lesson learned |
|---------|----------|--------------------|
| _Parking Lot_ | | |

---

## Design Principles

Two buckets: **General software principles** + **OOD principles (SOLID)**.
Interviewers care that you APPLY them, not that you can name them.

### General (remember these 3 above all: KISS, DRY, YAGNI)

**KISS — Keep It Simple, Stupid**
- Simplest thing that works = usually right. Plain class first; add patterns only when simplicity breaks.
- Over-engineering to show off is the #1 ding in LLD interviews.
- Add complexity when: class grows huge / a change forces edits in 5 places.

**DRY — Don't Repeat Yourself**
- It's about repeated **knowledge**, not repeated text. Same *concept* → merge. Just *looks* similar → leave it.
- Wrong merge = coupling trap: editing the shared fn for purpose A silently breaks purpose B.
- "Duplication is cheaper than the wrong abstraction."

**YAGNI — You Aren't Gonna Need It**
- Build only what's needed now. Extra features later.
- **Design with extension in mind, but don't BUILD ahead.** (Think-ahead yes, build-ahead no.)

> ⚡ **KISS vs DRY tension** (the senior signal): they fight. KISS = don't abstract; DRY = don't duplicate.
> Say the tradeoff out loud: *"I'll keep this in the User class for now (KISS); if it appears 3–4 times, I'll extract a validator (DRY)."*

**Separation of Concerns** — each part handles one responsibility, doesn't know others' internals (UI ≠ business logic ≠ data). Lets you swap/test each part independently.

**Law of Demeter** — talk to immediate friends only. `order.getCustomer().getAddress().getZip()` ❌ leaks internal structure → add `order.getCustomerZip()`. (Fluent builders returning same type are fine.)

### OOD — SOLID (to fill in after I read it)

- **S** — _Single Responsibility_: ...
- **O** — Open/Closed: open for extension, closed for modification → new class > edited class.
- **L** — _Liskov Substitution_: ...
- **I** — _Interface Segregation_: ...
- **D** — _Dependency Inversion_: ...
