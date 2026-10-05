# personal-projects

A collection of hardware-engineering tools, ML performance studies, RTL designs, and architecture notes by **zesun33**.

The projects connect two goals: understand how computation and data movement affect performance, and make hardware development easier to review, test, and reproduce. Some repositories provide usable tools; others are learning exercises or plans for future implementations.

## Find your starting point

| I want to… | Start with | First useful result |
|---|---|---|
| Try the hardware-agent tools | [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold) | A starter counter design, testbench, and MCP client configuration |
| Understand how the tools fit together | [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) | A small RTL review → simulation → synthesis walkthrough |
| Compare GPU matrix-multiplication performance | [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization) | Correctness checks and a documented naive/tiled/cuBLAS comparison |
| Generate and profile a CUDA kernel | [kernel-forge](https://github.com/zesun33/kernel-forge) | Device information, a kernel template, and timing/model reports |
| Study event-driven neuromorphic RTL | [lif-spiking-core](https://github.com/zesun33/lif-spiking-core) | Neuron/tile/router source, testbenches, and verification notes |
| Learn or discuss the unfinished projects | [PROJECT_GUIDE.md](PROJECT_GUIDE.md) | Clear exercise, architecture-draft, and roadmap boundaries |

Read [GETTING_STARTED.md](GETTING_STARTED.md) for prerequisites, a first working example, and a glossary. The [project guide](PROJECT_GUIDE.md) explains who each repository is for, what to try first, and what currently exists.

- Website: [zesun33.github.io](https://zesun33.github.io)
- Landing page for the agent-tooling family: [zesun33/hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling)

You can use any individual repository directly. Clone this catalog when you want the full project map and local workspace:

```bash
git clone https://github.com/zesun33/personal-projects.git
cd personal-projects
```

Open `personal-projects.code-workspace` in Cursor / VS Code for a multi-root workspace over the local checkouts below.

## Organization and consistency

[`projects.json`](projects.json) owns repository metadata. Generate workspace profiles, project tables, status, and checkout ignores from it:

```bash
python3 scripts/generate_catalog.py
python3 scripts/generate_project_guides.py
python3 scripts/check_catalog.py
python3 scripts/check_catalog.py --network
```

Use `--catalog-only` for a fresh parent clone or CI without child checkouts. README orientation sections and `PROJECT_GUIDE.md` share the `guide` metadata in `projects.json`; `generate_project_guides.py` updates only marked sections and preserves the rest of each README. Use its `--check` option to inspect drift. See [`STATUS.md`](STATUS.md) for maturity/next milestones, [`DEPENDENCIES.md`](DEPENDENCIES.md) for project relationships, and [`SYNC.md`](SYNC.md) for the cross-machine workflow.

See [`UPGRADES.md`](UPGRADES.md) for portable GPU selection, measured GEMM comparisons, hardware evidence definitions, and npm release automation.

See [`NPM_RELEASES.md`](NPM_RELEASES.md) for batch trusted-publisher setup and separate release workflows for the ten published npm packages.

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
| [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) | Find and choose the hardware-agent tools in this portfolio | shipped | GitHub source |
| [eda-docker-images](https://github.com/zesun33/eda-docker-images) | Run open-source hardware tools in shared Docker or Podman images | shipped | GitHub source |
| [eda-devcontainer](https://github.com/zesun33/eda-devcontainer) | Develop hardware projects in editor containers backed by EDA images | shipped | GitHub source |
| [mcp-verilog](https://github.com/zesun33/mcp-verilog) | Lint, compile, and simulate Verilog/SystemVerilog through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-verilog) |
| [hw-agent-skills](https://github.com/zesun33/hw-agent-skills) | Apply hardware-review and verification rubrics through coding-agent instruction files | shipped | Source files (no npm package) |
| [hw-verification-suite](https://github.com/zesun33/hw-verification-suite) | Reuse Python testbench components for LIF neuron tiles and AER routing | shipped | GitHub source |
| [mcp-cocotb](https://github.com/zesun33/mcp-cocotb) | Run Python hardware testbenches and inspect their results through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-cocotb) |
| [mcp-yosys](https://github.com/zesun33/mcp-yosys) | Inspect synthesis, hierarchy, and unintended latches before physical design through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-yosys) |
| [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review) | Review RTL assignment, width, and reset rules before simulation through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-rtl-review) |
| [mcp-openroad](https://github.com/zesun33/mcp-openroad) | Run physical-design stages and inspect timing for a netlist through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-openroad) |
| [mcp-gds](https://github.com/zesun33/mcp-gds) | Inspect layouts, stream out GDS, and run geometry or netlist checks through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-gds) |
| [mcp-formal](https://github.com/zesun33/mcp-formal) | Check assertions and run bounded or inductive RTL proofs through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-formal) |
| [mcp-fpga](https://github.com/zesun33/mcp-fpga) | Synthesize and route FPGA designs and prepare bitstreams through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-fpga) |
| [mcp-spice](https://github.com/zesun33/mcp-spice) | Run ngspice circuit netlists and retrieve measurement results through an MCP server | shipped | [npm](https://www.npmjs.com/package/@zesun33/mcp-spice) |
| [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold) | Create a starter RTL project and configuration for nine hardware MCP servers | shipped | [npm](https://www.npmjs.com/package/@zesun33/create-hw-agent) |
| [gh-actions-for-hw](https://github.com/zesun33/gh-actions-for-hw) | Run hardware checks through reusable GitHub Actions | shipped | GitHub source |
| [kernel-forge](https://github.com/zesun33/kernel-forge) | Generate CUDA kernel templates and inspect correctness, timing, and modeled Roofline limits | shipped | GitHub source |
| [agentic-asic](https://github.com/zesun33/agentic-asic) | Coordinate RTL review, verification, synthesis, and implementation through EDA MCP servers | shipped | GitHub source |

## ML systems

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization) | Compare correctness and measured FP32 throughput across naive, tiled, and cuBLAS GEMM | active | GitHub source |
| [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark) | Learn CUDA memory behavior through notes and a bandwidth exercise scaffold | active | GitHub source |
| [parallel-computing-lab](https://github.com/zesun33/parallel-computing-lab) | Learn CPU parallelism by completing OpenMP exercises | active | GitHub source |
| [resnet-tensorrt-bench](https://github.com/zesun33/resnet-tensorrt-bench) | Plan a future ResNet inference study comparing precision, latency, and accuracy | planned | GitHub source |
| [triton-flash-attention-lite](https://github.com/zesun33/triton-flash-attention-lite) | Plan a future tiled-attention implementation and correctness/performance study | planned | GitHub source |

## Silicon designs

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [lif-spiking-core](https://github.com/zesun33/lif-spiking-core) | Study and simulate LIF neuron tiles, AER routing, and a 2x2 neuromorphic mesh | shipped | GitHub source |
| [cim-bit-serial-pe](https://github.com/zesun33/cim-bit-serial-pe) | Specify a proposed bit-serial compute-in-memory processing element | planned | GitHub source |
| [neuro-cim-tile](https://github.com/zesun33/neuro-cim-tile) | Specify a proposed compute-in-memory tile and its digital/device-model boundaries | planned | GitHub source |
| [tiny-tpu-systolic-array](https://github.com/zesun33/tiny-tpu-systolic-array) | Specify a proposed INT8 systolic-array dataflow and interface | planned | GitHub source |

## Rust systems

| Project | Purpose | Maturity | Distribution |
|---|---|---|---|
| [rust-systems-track](rust-systems-track/README.md) | Follow private Rust fundamentals toward planned GEMM and LIF/AER systems projects | learning | Catalog metadata; basics private |

Rust path: private Phase 0 basics → future public `rust-quant-gemm` → future public `lif-rust-golden` co-checked against `lif-spiking-core`. See [PLAN](rust-systems-track/PLAN.md) and [TRACKER](rust-systems-track/TRACKER.md). Private drill solutions are never cataloged as public projects.

<!-- END GENERATED PROJECT CATALOG -->

## Layout

Locally, sibling repos live under this directory (each with its own `.git`). The parent ignores those directories so they are not nested gitlinks. See [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) for the agent-tooling roadmap and [zesun33.github.io](https://zesun33.github.io) for the personal site.
