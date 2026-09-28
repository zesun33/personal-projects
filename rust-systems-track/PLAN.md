# Rust Systems Track — Plan

Curriculum for systems-engineering Rust: private basics → one public systems bridge → domain flagship co-verification against `lif-spiking-core`.

Living progress: [TRACKER.md](TRACKER.md). Index: [README.md](README.md).

## Decisions (locked)

- Basics stay **private** (never website / showcase table).
- One medium bridge: quantized / bit-exact CPU GEMM (`rust-quant-gemm`).
- Domain flagship: Rust LIF/AER golden model (`lif-rust-golden`) bit-exact vs RTL.
- No generic multi-demo Rust portfolio; no MCP rewrites in Rust; no CUDA-in-Rust.

---

## Phase 0 — Basics (private, full detail)

**Directory:** `00-basics/` → private GitHub `zesun33/rust-basics` (or similar).

**Depth:** learn **every** Book chapter (including advanced ch.19, concurrency, macros, async overview) — no skimming for “speed.” Chapter checklist + mastery criteria: [`00-basics/notes/SYLLABUS.md`](00-basics/notes/SYLLABUS.md).

### Work

1. Install toolchain: `rustup`, `cargo`, `rust-analyzer`, `clippy`, `rustfmt`.
2. The Rust Book **cover to cover** — for each chapter: read → type examples → note file under `00-basics/notes/chXX_*.md` → matching rustlings.
3. Complete **all** rustlings under `00-basics/rustlings/`.
4. Cargo drills under `00-basics/drills/` (required + chapter practice crates):
   - chapter practice: `ch01_hello`, guessing game, etc.
   - parse / `Result` pipeline
   - slice views / lifetimes intuition
   - `Rc`/`RefCell` vs ownership redesign
   - trait objects vs generics
   - file I/O + serde JSON
   - ring buffer with unit tests
   - (optional) simple CLI with clap

### Exit criteria

- Can explain borrow-checker errors, lifetimes, `Send`/`Sync` intuition, and when `unsafe` is needed — without hand-waving
- Comfortable with `cargo test`, `clippy`, reading std docs and The Nomicon (skimmed with intent)
- **No** public README or portfolio claim for this phase

### Git

```bash
cd 00-basics
git init
# create PRIVATE repo zesun33/rust-basics — do not list on website
```

---

## Phase 1 — Systems bridge (public after exit)

**Directory:** `01-systems-bridge/` → public `rust-quant-gemm`.

Scaffold only until Phase 0 exit. Then implement:

- Packed INT8 / INT4 (or Q8_0-style) matmul on CPU
- Explicit memory-layout docs
- Naive + blocked kernels
- `proptest` vs f32 or fixed-point golden (bit-exact or documented bounds)
- Criterion benches; roofline-style notes linking vocabulary from `cuda-gemm-optimization` / `kernel-forge`

### Exit criteria

- CI: `cargo test`, `clippy`, `fmt`
- README with measured numbers
- Any `unsafe` documented and minimized

Then: public GitHub, parent README Family 4 row, workspace folder, `.gitignore` sibling entry.

---

## Phase 2 — Domain flagship (public after exit)

**Directory:** `02-domain-lif-golden/` → public `lif-rust-golden`.

Scaffold only until Phase 1 exit. Then implement:

- Step- or cycle-accurate LIF + AER packet model in safe Rust
- Stimulus/response vectors compared against `lif-spiking-core` cocotb/PyUVM paths
- Stretch (same repo): JSON vector exchange or thin FFI so Python TB can compare

### Exit criteria

- Architecture note
- Bit-exact or explicitly bounded mismatch report
- CI for Rust tests
- README ties to existing Nangate45 / mesh story

Publish and catalog like other silicon projects.

---

## Visibility summary

| Phase | Path | GitHub | Showcase |
|-------|------|--------|----------|
| 0 | `00-basics` | Private | No |
| 1 | `01-systems-bridge` | Public after exit | Yes |
| 2 | `02-domain-lif-golden` | Public after exit | Yes |
