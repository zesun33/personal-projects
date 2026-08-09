# personal-projects

Meta catalog and multi-root workspace for **zesun33** public learning and HW agent tooling repos.

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

```bash
git clone https://github.com/zesun33/hw-agent-tooling.git
git clone https://github.com/zesun33/eda-docker-images.git
git clone https://github.com/zesun33/eda-devcontainer.git
```

> **Note:** [zesun33/eda](https://github.com/zesun33/eda) is an older private monorepo and is **archived**. Prefer `eda-docker-images` and `eda-devcontainer`.

---

## Family 2 — ML systems practice

Learning-focused repos covering CUDA kernels, memory systems, OpenMP, TensorRT, and Triton.

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

## Layout

Locally, sibling repos live under this directory (each with its own `.git`). The parent ignores those directories so they are not nested gitlinks. See [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) for the agent-tooling roadmap and [zesun33.github.io](https://zesun33.github.io) for the personal site.
