# Portfolio status

Generated from `projects.json` by `python3 scripts/generate_catalog.py`.

Maturity reflects the repository roadmap. It is not a fresh test result, silicon fabrication claim, or physical signoff verdict.

| Family | Shipped | Active | Planned | Learning |
|---|---:|---:|---:|---:|
| Hardware agent tooling | 18 | 0 | 0 | 0 |
| ML systems | 0 | 3 | 2 | 0 |
| Silicon designs | 1 | 3 | 0 | 0 |
| Rust systems | 0 | 0 | 0 | 1 |

| Project | Status | Verification entry point | Next milestone |
|---|---|---|---|
| [hw-agent-tooling](hw-agent-tooling/README.md) | shipped | `./scripts/verify.sh --quick` | Maintain regression coverage and distribution consistency |
| [eda-docker-images](eda-docker-images/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [eda-devcontainer](eda-devcontainer/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-verilog](mcp-verilog/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [hw-agent-skills](hw-agent-skills/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [hw-verification-suite](hw-verification-suite/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-cocotb](mcp-cocotb/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-yosys](mcp-yosys/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-rtl-review](mcp-rtl-review/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-openroad](mcp-openroad/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-gds](mcp-gds/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-formal](mcp-formal/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-fpga](mcp-fpga/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [mcp-spice](mcp-spice/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [hw-agent-scaffold](hw-agent-scaffold/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [gh-actions-for-hw](gh-actions-for-hw/README.md) | shipped | not configured | Maintain regression coverage and distribution consistency |
| [kernel-forge](kernel-forge/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [agentic-asic](agentic-asic/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [cuda-gemm-optimization](cuda-gemm-optimization/README.md) | active | `make all` → `./build/01_naive_gemm 512 512 512` | Extend the measured GEMM optimization ladder |
| [cuda-memory-benchmark](cuda-memory-benchmark/README.md) | active | not configured | Implement access-pattern and shared-memory benchmarks |
| [parallel-computing-lab](parallel-computing-lab/README.md) | active | not configured | Implement reductions and synchronization exercises |
| [resnet-tensorrt-bench](resnet-tensorrt-bench/README.md) | planned | not configured | Implement model export and a measured TensorRT baseline |
| [triton-flash-attention-lite](triton-flash-attention-lite/README.md) | planned | not configured | Implement and check the first attention kernel |
| [lif-spiking-core](lif-spiking-core/README.md) | shipped | `./scripts/verify.sh` | Maintain regression coverage and distribution consistency |
| [cim-bit-serial-pe](cim-bit-serial-pe/README.md) | active | not configured | Complete self-checking precision and zero-skipping regression |
| [neuro-cim-tile](neuro-cim-tile/README.md) | active | not configured | Complete digital-periphery and device-model checks |
| [tiny-tpu-systolic-array](tiny-tpu-systolic-array/README.md) | active | not configured | Complete GEMM/dataflow regression |
| [rust-systems-track](rust-systems-track/README.md) | learning | learning | Finish Book chapters 1–2 and rustlings intro/variables (private) |
