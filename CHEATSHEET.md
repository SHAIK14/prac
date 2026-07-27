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

| Problem | Status | Key lesson learned |
|---------|--------|--------------------|
| Connect 4 (game) | ✅ done | board model + game loop; flicker-free render = build full frame, print once |
| API Rate Limiter (tier-based) | ✅ done | 2 axes (strategy × tier) → 2-level config; instance-per-client; Singleton = shared state; lazy refill (token bucket) |
| KV Cache / Mini Redis (TTL) | ✅ done | store deadline (now+sec) not duration; lazy delete (in get) + active sweeper; daemon thread; lock get too (it deletes) |
| LRU / LFU eviction | 🔜 do in DSA | hashmap + doubly-linked-list O(1); in LLD wrap behind `EvictionPolicy` Strategy (OrderedDict shortcut) |
| _Parking Lot_ | 🔜 next | |

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
- **D** — _Dependency Inversion_: depend on the interface (`RateLimitStrategy`/`EvictionPolicy`), not the concrete class. Factory hides which concrete one.

---

## Concurrency in Python (learned via Rate Limiter + Redis)

**The GIL** — only ONE thread runs Python bytecode at a time. So Python threads:
- give **I/O concurrency** (while one waits on DB/network, another runs) — NOT CPU parallelism
- for true CPU parallelism → `multiprocessing` (separate processes)

**Why locks still needed despite GIL:** the GIL switches threads *mid-operation*. `tokens -= 1` = read→subtract→write (3 steps); a switch between them = race. Lock makes the read-modify-write atomic.

**`threading.Lock`** (= Go's `sync.Mutex`):
- `with self.lock:` = auto acquire/release (like Go's `defer mu.Unlock()`)
- lock the **smallest critical section**; one lock per independent shared state (per-client > one global = more concurrency)
- **lock reads too IF they mutate** (e.g. cache `get` does lazy-delete → must lock)
- **non-reentrant**: a thread can't re-acquire a lock it holds → helper called inside a locked section must NOT re-lock (deadlock). Use `RLock` if you must.
- **never hold a lock across `sleep`/blocking calls** (freezes everyone)

**Background thread** (active sweeper): `threading.Thread(target=self._sweep, daemon=True).start()`
- `.start()` (NOT `.run()` — run() blocks on current thread)
- `daemon=True` = dies when main exits (else `while True` hangs program)
- `.join()` = wait for it (Go WaitGroup). `args=(...)` = pass params.

**Go → Python:** goroutine→Thread/asyncio · channel→queue.Queue · Mutex→Lock · RWMutex→(none built-in) · WaitGroup→join.

---

## TTL / Expiration (Mini Redis)

- store the **deadline** = `time.time() + ttl_seconds` (absolute), NOT the duration. Check: `now >= deadline → expired`.
- **Lazy deletion** (in `get`): on read, if expired → delete, return None. = correctness (never serve stale).
- **Active sweeper** (background thread): periodically scan & delete expired. = memory reclamation (don't leak untouched keys).
- **Need BOTH.** Lazy alone leaks; active alone may serve stale + costs full scans.
- Gotcha: `for k in list(d.items())` — can't mutate dict mid-iteration; snapshot with `list()`.

---

## Python gotchas (bit me)

- **dunders spelled EXACTLY**: `__init__` (not `__init`/`__int__`) — Python won't warn, just never calls it.
- **Singleton `__init__` re-runs** even when `__new__` returns cached instance → wipes state. Guard: `if hasattr(self, "x"): return`.
- **dict access**: `d[k]` crashes if absent; `d.get(k)`/`d.pop(k, None)` safe. Use `del` when you KNOW it exists, `pop(k,None)` when maybe.
- **enum as key** (Tier/StrategyType) = typo fails at parse, not runtime. Class=PascalCase, members=UPPERCASE.
- **`<` vs `<=`**: off-by-one. "exactly N allowed" → `count < limit`.
- **imports**: absolute (`from pkg.mod import X`), run with `python3 -m pkg.main` from project root. Every folder needs `__init__.py`.

---

## Recommended next LLDs (30-min, reuse this method)

| Problem | Why / what's new |
|---------|------------------|
| **Parking Lot** | the classic — entities/inheritance (vehicle types, spot types), Strategy for pricing |
| **Elevator System** | state machine + scheduling Strategy; request queue |
| **Vending Machine** | State pattern (idle/paid/dispensing); clean state transitions |
| **Notification Service** | Strategy (email/SMS/push) + Factory — almost identical to your rate limiter shape |
| **Splitwise / Expense Share** | entity modeling + split Strategy (equal/exact/percent) |
| **Logging Framework** | Chain of Responsibility (log levels) + Strategy (sinks) |
| **Tic-Tac-Toe / Chess** | board + rules + win-check; you've done Connect4, similar |
