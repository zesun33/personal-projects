# Portfolio status

Generated from `projects.json` by `python3 scripts/generate_catalog.py`.

Maturity reflects the repository roadmap. It is not a fresh test result, silicon fabrication claim, or physical signoff verdict.

| Family | Shipped | Active | Planned | Learning |
|---|---:|---:|---:|---:|
| Hardware agent tooling | 18 | 0 | 0 | 0 |
| ML systems | 0 | 3 | 2 | 0 |
| Silicon designs | 1 | 0 | 3 | 0 |
| Rust systems | 0 | 0 | 0 | 1 |

| Project | Status | Verification entry point | Next milestone |
|---|---|---|---|
| [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling) | shipped | `./scripts/verify.sh --quick` | Maintain regression coverage and distribution consistency |
| [eda-docker-images](https://github.com/zesun33/eda-docker-images) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [eda-devcontainer](https://github.com/zesun33/eda-devcontainer) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-verilog](https://github.com/zesun33/mcp-verilog) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [hw-agent-skills](https://github.com/zesun33/hw-agent-skills) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [hw-verification-suite](https://github.com/zesun33/hw-verification-suite) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-cocotb](https://github.com/zesun33/mcp-cocotb) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-yosys](https://github.com/zesun33/mcp-yosys) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-openroad](https://github.com/zesun33/mcp-openroad) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-gds](https://github.com/zesun33/mcp-gds) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-formal](https://github.com/zesun33/mcp-formal) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-fpga](https://github.com/zesun33/mcp-fpga) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-spice](https://github.com/zesun33/mcp-spice) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [gh-actions-for-hw](https://github.com/zesun33/gh-actions-for-hw) | shipped | not configured | Maintain regression coverage and distribution consistency |
| [kernel-forge](https://github.com/zesun33/kernel-forge) | shipped | `./scripts/verify.sh` | Expand measured kernel cases and GPU reference coverage |
| [agentic-asic](https://github.com/zesun33/agentic-asic) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization) | active | `./scripts/verify.sh` | Add register tiling and repeat the checked performance comparison |
| [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark) | active | not configured | Complete and correctness-check the existing global-memory bandwidth exercise |
| [parallel-computing-lab](https://github.com/zesun33/parallel-computing-lab) | active | not configured | Implement reductions and synchronization exercises |
| [resnet-tensorrt-bench](https://github.com/zesun33/resnet-tensorrt-bench) | planned | not configured | Implement model export and a measured TensorRT baseline |
| [triton-flash-attention-lite](https://github.com/zesun33/triton-flash-attention-lite) | planned | not configured | Implement and check the first attention kernel |
| [lif-spiking-core](https://github.com/zesun33/lif-spiking-core) | shipped | `./scripts/verify.sh` | Capture versioned timing reports and tool manifests for implementation results |
| [cim-bit-serial-pe](https://github.com/zesun33/cim-bit-serial-pe) | planned | not configured | Implement the documented arithmetic in RTL and check it against a software reference |
| [neuro-cim-tile](https://github.com/zesun33/neuro-cim-tile) | planned | not configured | Implement and verify the digital periphery before adding calibrated device models |
| [tiny-tpu-systolic-array](https://github.com/zesun33/tiny-tpu-systolic-array) | planned | not configured | Implement a small array and check its dataflow against a GEMM reference |
| [rust-systems-track](rust-systems-track/README.md) | learning | learning | Finish Book chapters 1–2 and rustlings intro/variables (private) |
