# Rust Systems Track — Tracker

> **Update this file at the end of every agent turn** that mentions Rust learning, this track, Phase 0/1/2, or edits under `rust-systems-track/`.
> Do not put private drill solutions or long notes here — only status.

## Current phase

- **Phase:** `0`
- **Status:** `in_progress`

## Last session

- **Date:** 2026-10-01
- **Done:** Reviewed the Rust plan during portfolio organization; added a focused workspace and cross-machine catalog support. No learning milestones completed. The offline Book setup from 2026-09-14 remains documented in `00-basics/BOOK.md`.
- **Blockers:** none

## Next action

Open `00-basics/book-html/ch01-00-getting-started.html` (or online Book); finish ch.1–2 + rustlings intro/variables; mark TRACKER Book boxes.

## Checklist

### Phase 0 — Tooling

- [x] `rustup` / `cargo` / rust-analyzer / clippy / rustfmt installed
- [x] rustlings cloned into `00-basics/rustlings/`
- [x] Full-detail syllabus written (`notes/SYLLABUS.md`)

### Phase 0 — Book (every chapter)

- [ ] Ch 1 Getting Started (+ `ch01_hello`)
- [ ] Ch 2 Guessing Game
- [ ] Ch 3 Common Programming Concepts
- [ ] Ch 4 Ownership
- [ ] Ch 5 Structs
- [ ] Ch 6 Enums & Pattern Matching
- [ ] Ch 7 Packages, Crates, Modules
- [ ] Ch 8 Common Collections
- [ ] Ch 9 Error Handling
- [ ] Ch 10 Generics, Traits, Lifetimes
- [ ] Ch 11 Writing Automated Tests
- [ ] Ch 12 I/O project
- [ ] Ch 13 Closures & Iterators
- [ ] Ch 14 Cargo & Crates.io
- [ ] Ch 15 Smart Pointers
- [ ] Ch 16 Fearless Concurrency
- [ ] Ch 17 OOP features
- [ ] Ch 18 Patterns & Matching
- [ ] Ch 19 Advanced Features (unsafe, advanced traits/types, macros)
- [ ] Ch 20 Final project (read + optional implement)
- [ ] Async overview (Book / async book enough to not fear `.await`)
- [ ] Appendices (keywords, operators, derivable traits)

### Phase 0 — Rustlings & drills

- [ ] rustlings completed (all sections)
- [ ] Drill: parse / `Result` pipeline
- [ ] Drill: slice views
- [ ] Drill: `Rc`/`RefCell` vs ownership redesign
- [ ] Drill: trait objects vs generics
- [ ] Drill: file I/O + serde JSON
- [ ] Drill: ring buffer + tests
- [ ] Private git repo created (not showcased)
- [ ] Phase 0 exit criteria met

### Phase 1 — Systems bridge (`rust-quant-gemm`)

- [ ] Layout docs + INT8/INT4 (or Q8_0) matmul design
- [ ] Naive kernel
- [ ] Blocked kernel
- [ ] `proptest` / golden checks
- [ ] Criterion benches + numbers in README
- [ ] CI (test, clippy, fmt)
- [ ] Public repo + catalog row
- [ ] Phase 1 exit criteria met

### Phase 2 — Domain flagship (`lif-rust-golden`)

- [ ] LIF + AER golden model in Rust
- [ ] Vector dump/compare vs `lif-spiking-core` TB
- [ ] Architecture note + mismatch report
- [ ] CI
- [ ] Public repo + catalog row
- [ ] Phase 2 exit criteria met

## Decisions log

- **2026-09-14:** Track created. Basics private; bridge = quantized GEMM; flagship = LIF golden vs RTL.
- **2026-09-14:** User requested **every detail** — Phase 0 is cover-to-cover Book + all rustlings (no skim of ch.19/async).

## Do not showcase

`00-basics` stays **private**. Never add it to the website or the public personal-projects showcase table.
