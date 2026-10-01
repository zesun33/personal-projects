# Project relationships

```mermaid
flowchart TD
    images[eda-docker-images] --> devcontainer[eda-devcontainer]
    images --> servers[Nine EDA MCP servers]
    servers --> scaffold[hw-agent-scaffold]
    servers --> asic[agentic-asic]
    skills[hw-agent-skills] --> asic
    images --> actions[gh-actions-for-hw]
    vip[hw-verification-suite] --> lif[lif-spiking-core]
    cuda[CUDA GEMM and memory labs] --> forge[kernel-forge]
    cuda -. planned learning bridge .-> quant[rust-quant-gemm]
    lif -. planned co-verification .-> golden[lif-rust-golden]
```

Arrows show tool, runtime, or learning relationships, not npm dependency declarations. `agentic-asic` orchestrates the ASIC subset of servers; FPGA and SPICE servers are also distributed by the scaffold. The Rust public repositories are future phases. Private Rust fundamentals remain outside the public showcase.
