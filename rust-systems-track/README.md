# Rust Systems Track

Meta catalog for learning Rust and showcasing it in ML systems / neuromorphic HW–SW codesign.

Path: `personal-projects/rust-systems-track/`

## Path (locked)

1. **Phase 0 — Basics** (`00-basics/`) — private only; never a portfolio showcase
2. **Phase 1 — Systems bridge** (`01-systems-bridge/` → public `rust-quant-gemm`) — one medium quantized GEMM crate
3. **Phase 2 — Domain flagship** (`02-domain-lif-golden/` → public `lif-rust-golden`) — Rust LIF/AER golden model vs `lif-spiking-core`

Do **not** build a long ladder of generic Rust demos. Details: [PLAN.md](PLAN.md).

## Progress tracking (required)

| File | Role |
|------|------|
| [TRACKER.md](TRACKER.md) | Living checklist — **update every agent turn** that touches this track |
| [PLAN.md](PLAN.md) | Curriculum, exit criteria, visibility |
| `../.memory/rust-systems-track.md` | Local durable memory (gitignored) |
| `../.cursor/rules/rust-systems-track.mdc` | Agent rule: read PLAN+TRACKER first; update TRACKER before ending |

**Agent / human duty:** After any work on Rust learning or this directory, update `TRACKER.md` (last session, checklist, next action). When phase or next-action changes, mirror a short status line into `.memory/rust-systems-track.md`.

## Visibility

| Path | GitHub | Showcase |
|------|--------|----------|
| `00-basics` | Private only (`zesun33/rust-basics` or similar) | **No** |
| `01-systems-bridge` | Public after exit criteria | Yes (ML systems / Rust) |
| `02-domain-lif-golden` | Public after exit criteria | Yes (neuromorphic / codesign) |

## Layout

```text
rust-systems-track/
  README.md PLAN.md TRACKER.md   # meta (tracked with parent catalog)
  resources/                     # reading list
  00-basics/                     # private learning (own git later)
  01-systems-bridge/             # scaffold → rust-quant-gemm
  02-domain-lif-golden/          # scaffold → lif-rust-golden
```

Meta files (`README`, `PLAN`, `TRACKER`, `resources/`) stay in this catalog. Phase directories become standalone repos and are ignored by the parent once they have their own `.git`.

## Out of scope

- Rewriting MCP / TypeScript EDA servers in Rust
- CUDA kernels in Rust (keep CUDA/Triton)
