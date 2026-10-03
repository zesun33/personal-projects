# personal-projects

Meta catalog and multi-root workspace for **zesun33** public ML systems and HW agent tooling repos.

- Website: [zesun33.github.io](https://zesun33.github.io)
- Landing page for the agent-tooling family: [zesun33/hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling)

Clone this catalog (optional — each project is also a standalone repo):

```bash
git clone https://github.com/zesun33/personal-projects.git
cd personal-projects
```

Open `personal-projects.code-workspace` in Cursor / VS Code for a multi-root workspace over the local checkouts below.

## Organization and consistency

[`projects.json`](projects.json) owns repository metadata. Generate workspace profiles, project tables, status, and checkout ignores from it:

```bash
python3 scripts/generate_catalog.py
python3 scripts/check_catalog.py
python3 scripts/check_catalog.py --network
```

Use `--catalog-only` for a fresh parent clone or CI without child checkouts. See [`STATUS.md`](STATUS.md) for maturity/next milestones, [`DEPENDENCIES.md`](DEPENDENCIES.md) for project relationships, and [`SYNC.md`](SYNC.md) for the cross-machine workflow.

See [`UPGRADES.md`](UPGRADES.md) for portable GPU selection, measured GEMM comparisons, hardware evidence definitions, and npm release automation.

Each project keeps a separate GitHub repository and Git history. After pulling the parent on another machine, clone/pull the child repositories separately:

```bash
git pull --ff-only
python3 scripts/sync_projects.py --clone-missing --pull --dry-run
python3 scripts/sync_projects.py --clone-missing --pull
```

The sync helper leaves dirty or divergent repositories untouched. Private Rust basics, local notes, caches, container images, and installed packages are not transferred by the catalog pull.

| Workspace | Focus |
|---|---|
| [`personal-projects.code-workspace`](personal-projects.code-workspace) | All catalog projects |
| [`hardware-agent.code-workspace`](hardware-agent.code-workspace) | MCP servers, skills, EDA runtimes, scaffold, CI, and orchestrator |
| [`silicon-designs.code-workspace`](silicon-designs.code-workspace) | Neuromorphic/CIM/systolic designs and supporting tools |
| [`ml-systems.code-workspace`](ml-systems.code-workspace) | CUDA, memory systems, OpenMP, TensorRT, Triton, and kernel-forge |
| [`rust-track.code-workspace`](rust-track.code-workspace) | Rust curriculum metadata and private learning path |

The runner reads verification commands from the catalog and reports uncovered projects separately:

```bash
./scripts/verify_portfolio_full.sh --list
./scripts/verify_portfolio_full.sh --project hw-agent-scaffold
python3 scripts/check_npm.py
```

Full EDA/GPU tests have runtime prerequisites. The RTL-review backend fix and published npm release are recorded in [`SYNC.md`](SYNC.md#rtl-review-runtime-compatibility-released-as-022-on-2026-10-01).

<!-- BEGIN GENERATED PROJECT CATALOG -->

## Hardware agent tooling

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) | Landing page, roadmap, and verification for the agent-tooling family | shipped | GitHub source |
| [eda-docker-images](https://github.com/zesun33/eda-docker-images) | Docker/Podman images for Verilog, SPICE, FPGA, and ASIC open-source EDA | shipped | GitHub source |
| [eda-devcontainer](https://github.com/zesun33/eda-devcontainer) | VS Code / Cursor Dev Container profiles on those images | shipped | GitHub source |
| [mcp-verilog](https://github.com/zesun33/mcp-verilog) | Model Context Protocol server for Verilog/SystemVerilog linting, compilation, and simulation | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-verilog) |
| [hw-agent-skills](https://github.com/zesun33/hw-agent-skills) | Portable agent skills and rubrics for hardware engineering and ML systems | shipped | Source files (no npm package) |
| [hw-verification-suite](https://github.com/zesun33/hw-verification-suite) | Centralized IEEE 1800.2 PyUVM & Cocotb Verification IP (VIP) Suite for Neuromorphic & Accelerators | shipped | GitHub source |
| [mcp-cocotb](https://github.com/zesun33/mcp-cocotb) | Model Context Protocol server for Python-based Cocotb co-simulation testbenches | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-cocotb) |
| [mcp-yosys](https://github.com/zesun33/mcp-yosys) | Model Context Protocol server for Yosys RTL synthesis, cell statistics, and latch triage | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-yosys) |
| [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review) | Model Context Protocol server for AST-backed static RTL review, semantic bug detection, and code review scoring | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-rtl-review) |
| [mcp-openroad](https://github.com/zesun33/mcp-openroad) | Model Context Protocol server for OpenROAD physical design (floorplan, CTS, PDN, route, STA; Nangate45 + Sky130) | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-openroad) |
| [mcp-gds](https://github.com/zesun33/mcp-gds) | MCP server for GDS stream-out, KLayout DRC, Magic extract, and Netgen LVS | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-gds) |
| [mcp-formal](https://github.com/zesun33/mcp-formal) | MCP server for SymbiYosys formal prove / SVA lint | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-formal) |
| [mcp-fpga](https://github.com/zesun33/mcp-fpga) | MCP server for Yosys + nextpnr FPGA synth / P&R / bitstream | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-fpga) |
| [mcp-spice](https://github.com/zesun33/mcp-spice) | MCP server for ngspice batch circuit simulation | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-spice) |
| [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold) | One-step `npx @zesun33/create-hw-agent` installer | shipped | [npm](https://www.npmjs.com/package/@zesun33/create-hw-agent) |
| [gh-actions-for-hw](https://github.com/zesun33/gh-actions-for-hw) | Reusable GitHub Actions composites on GHCR EDA images | shipped | GitHub source |
| [kernel-forge](https://github.com/zesun33/kernel-forge) | Flagship developer CLI and Roofline benchmark runtime for GPU kernel engineering (CUDA & Triton) | shipped | GitHub source |
| [agentic-asic](https://github.com/zesun33/agentic-asic) | Autonomous silicon compilation and signoff orchestrator powered by EDA MCP servers | shipped | GitHub source |

## ML systems

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization) | Measured FP32 GEMM ladder: naive, shared-memory tiles, and cuBLAS baseline | active | GitHub source |
| [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark) | GPU memory hierarchy, bandwidth, and roofline | active | GitHub source |
| [parallel-computing-lab](https://github.com/zesun33/parallel-computing-lab) | OpenMP / CPU parallelism lab | active | GitHub source |
| [resnet-tensorrt-bench](https://github.com/zesun33/resnet-tensorrt-bench) | ResNet TensorRT FP32 / FP16 / INT8 benchmark path | planned | GitHub source |
| [triton-flash-attention-lite](https://github.com/zesun33/triton-flash-attention-lite) | FlashAttention-style kernels in Triton | planned | GitHub source |

## Silicon designs

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [lif-spiking-core](https://github.com/zesun33/lif-spiking-core) | Synthesizable 8x8 LIF Spiking Core Tile, 5-port AER Router, and 4-Core 2D Mesh SoC | shipped | GitHub source |
| [cim-bit-serial-pe](https://github.com/zesun33/cim-bit-serial-pe) | Bit-serial compute-in-memory processing element with precision scalability | active | GitHub source |
| [neuro-cim-tile](https://github.com/zesun33/neuro-cim-tile) | Neuromorphic mixed-signal / digital CIM macro with multi-bit synaptic crossbar | active | GitHub source |
| [tiny-tpu-systolic-array](https://github.com/zesun33/tiny-tpu-systolic-array) | Matrix multiplication systolic array engine with double-buffered weight stationary dataflow | active | GitHub source |

## Rust systems

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [rust-systems-track](rust-systems-track/README.md) | Private Rust fundamentals followed by quantized GEMM and an RTL-checked LIF/AER golden model | learning | Catalog metadata; basics private |

Rust path: private Phase 0 basics → future public `rust-quant-gemm` → future public `lif-rust-golden` co-checked against `lif-spiking-core`. See [PLAN](rust-systems-track/PLAN.md) and [TRACKER](rust-systems-track/TRACKER.md). Private drill solutions are never cataloged as public projects.

<!-- END GENERATED PROJECT CATALOG -->

## Layout

Locally, sibling repos live under this directory (each with its own `.git`). The parent ignores those directories so they are not nested gitlinks. See [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) for the agent-tooling roadmap and [zesun33.github.io](https://zesun33.github.io) for the personal site.
