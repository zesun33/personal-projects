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

---

## Family 1 — HW agent tooling

MCP servers, agent skills, CLIs, and shared EDA container foundations that help coding agents work on hardware and ML systems.

| Repo | Description | GitHub |
|------|-------------|--------|
| [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) | Landing page, roadmap, and verification for the agent-tooling family | [link](https://github.com/zesun33/hw-agent-tooling) |
| [eda-docker-images](https://github.com/zesun33/eda-docker-images) | Docker/Podman images for Verilog, SPICE, FPGA, and ASIC open-source EDA | [link](https://github.com/zesun33/eda-docker-images) |
| [eda-devcontainer](https://github.com/zesun33/eda-devcontainer) | VS Code / Cursor Dev Container profiles on those images | [link](https://github.com/zesun33/eda-devcontainer) |
| [mcp-verilog](https://github.com/zesun33/mcp-verilog) | Model Context Protocol server for Verilog/SystemVerilog linting, compilation, and simulation | [link](https://github.com/zesun33/mcp-verilog) |
| [hw-agent-skills](https://github.com/zesun33/hw-agent-skills) | Portable agent skills and rubrics for hardware engineering and ML systems | [link](https://github.com/zesun33/hw-agent-skills) |
| [hw-verification-suite](https://github.com/zesun33/hw-verification-suite) | Centralized IEEE 1800.2 PyUVM & Cocotb Verification IP (VIP) Suite for Neuromorphic & Accelerators | [link](https://github.com/zesun33/hw-verification-suite) |
| [mcp-cocotb](https://github.com/zesun33/mcp-cocotb) | Model Context Protocol server for Python-based Cocotb co-simulation testbenches | [link](https://github.com/zesun33/mcp-cocotb) |
| [mcp-yosys](https://github.com/zesun33/mcp-yosys) | Model Context Protocol server for Yosys RTL synthesis, cell statistics, and latch triage | [link](https://github.com/zesun33/mcp-yosys) |
| [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review) | Model Context Protocol server for AST-backed static RTL review, semantic bug detection, and code review scoring | [link](https://github.com/zesun33/mcp-rtl-review) |
| [mcp-openroad](https://github.com/zesun33/mcp-openroad) | Model Context Protocol server for OpenROAD physical design (floorplan, CTS, PDN, route, STA; Nangate45 + Sky130) | [link](https://github.com/zesun33/mcp-openroad) |
| [mcp-gds](https://github.com/zesun33/mcp-gds) | MCP server for GDS stream-out, KLayout DRC, Magic extract, and Netgen LVS | [link](https://github.com/zesun33/mcp-gds) |
| [mcp-formal](https://github.com/zesun33/mcp-formal) | MCP server for SymbiYosys formal prove / SVA lint | [link](https://github.com/zesun33/mcp-formal) |
| [mcp-fpga](https://github.com/zesun33/mcp-fpga) | MCP server for Yosys + nextpnr FPGA synth / P&R / bitstream | [link](https://github.com/zesun33/mcp-fpga) |
| [gh-actions-for-hw](https://github.com/zesun33/gh-actions-for-hw) | Reusable GitHub Actions composites on GHCR EDA images | [link](https://github.com/zesun33/gh-actions-for-hw) |
| [kernel-forge](https://github.com/zesun33/kernel-forge) | Flagship developer CLI and Roofline benchmark runtime for GPU kernel engineering (CUDA & Triton) | [link](https://github.com/zesun33/kernel-forge) |
| [agentic-asic](https://github.com/zesun33/agentic-asic) | Autonomous silicon compilation and signoff orchestrator powered by EDA MCP servers | [link](https://github.com/zesun33/agentic-asic) |

```bash
git clone https://github.com/zesun33/hw-agent-tooling.git
git clone https://github.com/zesun33/eda-docker-images.git
git clone https://github.com/zesun33/eda-devcontainer.git
git clone https://github.com/zesun33/mcp-verilog.git
git clone https://github.com/zesun33/hw-agent-skills.git
git clone https://github.com/zesun33/mcp-cocotb.git
git clone https://github.com/zesun33/mcp-yosys.git
git clone https://github.com/zesun33/mcp-rtl-review.git
git clone https://github.com/zesun33/mcp-openroad.git
git clone https://github.com/zesun33/mcp-gds.git
git clone https://github.com/zesun33/mcp-formal.git
git clone https://github.com/zesun33/mcp-fpga.git
git clone https://github.com/zesun33/gh-actions-for-hw.git
git clone https://github.com/zesun33/kernel-forge.git
git clone https://github.com/zesun33/agentic-asic.git
```

Images for the MCP servers are public on GHCR (`podman pull ghcr.io/zesun33/{verilog,asic,fpga,spice}:latest`). See each server README **Execution Runtime** section.
> **Note:** [zesun33/eda](https://github.com/zesun33/eda) is an older private monorepo and is **archived**. Prefer `eda-docker-images` and `eda-devcontainer`.

---

## Family 2 — ML systems

Repos covering CUDA kernels, memory systems, OpenMP, TensorRT, and Triton.

| Repo | Description | GitHub |
|------|-------------|--------|
| [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization) | CUDA GEMM from naive to Tensor Cores | [link](https://github.com/zesun33/cuda-gemm-optimization) |
| [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark) | GPU memory hierarchy, bandwidth, and roofline | [link](https://github.com/zesun33/cuda-memory-benchmark) |
| [parallel-computing-lab](https://github.com/zesun33/parallel-computing-lab) | OpenMP / CPU parallelism lab | [link](https://github.com/zesun33/parallel-computing-lab) |
| [resnet-tensorrt-bench](https://github.com/zesun33/resnet-tensorrt-bench) | ResNet TensorRT FP32 / FP16 / INT8 benchmark path | [link](https://github.com/zesun33/resnet-tensorrt-bench) |
| [triton-flash-attention-lite](https://github.com/zesun33/triton-flash-attention-lite) | FlashAttention-style kernels in Triton | [link](https://github.com/zesun33/triton-flash-attention-lite) |

```bash
git clone https://github.com/zesun33/cuda-gemm-optimization.git
git clone https://github.com/zesun33/cuda-memory-benchmark.git
git clone https://github.com/zesun33/parallel-computing-lab.git
git clone https://github.com/zesun33/resnet-tensorrt-bench.git
git clone https://github.com/zesun33/triton-flash-attention-lite.git
```

---

## Family 3 — Neuromorphic & Hardware Accelerator Silicon Designs

Synthesizable ASIC and FPGA cores for event-driven neuromorphic processing, compute-in-memory (CIM), and matrix accelerators.

| Repo | Description | Status | Verification & Tapeout |
|------|-------------|:---:|------------------------|
| [lif-spiking-core](https://github.com/zesun33/lif-spiking-core) | Synthesizable 8x8 LIF Spiking Core Tile, 5-port AER Router, and 4-Core 2D Mesh SoC | ✅ Shipped | 19/19 Tests PASS · 2D Mesh SoC + Router (465 MHz) · Nangate45 Tapeout Closed |
| [hw-verification-suite](https://github.com/zesun33/hw-verification-suite) | Centralized PyUVM and Cocotb VIP Verification Suite for Neuromorphic & Accelerators | ✅ Shipped | 4/4 Unit Tests PASS · Reusable AER & LIF VIP · CI Automated |
| [cim-bit-serial-pe](https://github.com/zesun33/cim-bit-serial-pe) | Bit-serial compute-in-memory processing element with precision scalability | 🚧 In Progress | Option 1B Architecture |
| [neuro-cim-tile](https://github.com/zesun33/neuro-cim-tile) | Neuromorphic mixed-signal / digital CIM macro with multi-bit synaptic crossbar | 🚧 In Progress | Option 1B Architecture |
| [tiny-tpu-systolic-array](https://github.com/zesun33/tiny-tpu-systolic-array) | Matrix multiplication systolic array engine with double-buffered weight stationary dataflow | 🚧 In Progress | Option 1B Architecture |

```bash
git clone https://github.com/zesun33/lif-spiking-core.git
git clone https://github.com/zesun33/hw-verification-suite.git
git clone https://github.com/zesun33/cim-bit-serial-pe.git
git clone https://github.com/zesun33/neuro-cim-tile.git
git clone https://github.com/zesun33/tiny-tpu-systolic-array.git
```

---

## Layout

Locally, sibling repos live under this directory (each with its own `.git`). The parent ignores those directories so they are not nested gitlinks. See [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) for the agent-tooling roadmap and [zesun33.github.io](https://zesun33.github.io) for the personal site.
