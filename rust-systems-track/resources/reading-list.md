# Reading list — Rust Systems Track

## Core (Phase 0)

- **Offline HTML (local):** `00-basics/book-html/index.html` — see `00-basics/BOOK.md`
- **Source clone:** `00-basics/book/` ([rust-lang/book](https://github.com/rust-lang/book))
- Online: [The Rust Programming Language (The Book)](https://doc.rust-lang.org/book/)
- [Rust By Example](https://doc.rust-lang.org/rust-by-example/)
- [Rustlings](https://github.com/rust-lang/rustlings) — under `../00-basics/rustlings/`
- [std docs](https://doc.rust-lang.org/std/) — learn to navigate, not memorize

## Systems / correctness (Phase 1 prep)

- [The Rustonomicon](https://doc.rust-lang.org/nomicon/) — skim before any `unsafe`
- [proptest book](https://altsysrq.github.io/proptest-book/)
- Criterion: [benches chapter](https://bheisler.github.io/criterion.rs/book/)

## Domain / inference (Phase 1–2)

- Candle (Hugging Face) — skim for tensor/runtime patterns: https://github.com/huggingface/candle
- PyO3 user guide — when bridging to Python research sims: https://pyo3.rs/
- Your existing notes: `cuda-gemm-optimization`, `kernel-forge`, `lif-spiking-core`

## Optional later

- Async book (only if serving / runtime I/O becomes relevant)
- Embedded Rust (only if bare-metal firmware enters scope)
