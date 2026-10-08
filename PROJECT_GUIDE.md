# Project guide

Choose a starting route in [GETTING_STARTED.md](GETTING_STARTED.md). This reference explains the audience, first task, result, and current scope of every catalog project.

Generated from `projects.json`; project README introductions use the same metadata.

## Index

- [hw-agent-tooling](#hw-agent-tooling)
- [eda-docker-images](#eda-docker-images)
- [eda-devcontainer](#eda-devcontainer)
- [mcp-verilog](#mcp-verilog)
- [hw-agent-skills](#hw-agent-skills)
- [hw-verification-suite](#hw-verification-suite)
- [mcp-cocotb](#mcp-cocotb)
- [mcp-yosys](#mcp-yosys)
- [mcp-rtl-review](#mcp-rtl-review)
- [mcp-openroad](#mcp-openroad)
- [mcp-gds](#mcp-gds)
- [mcp-formal](#mcp-formal)
- [mcp-fpga](#mcp-fpga)
- [mcp-spice](#mcp-spice)
- [hw-agent-scaffold](#hw-agent-scaffold)
- [gh-actions-for-hw](#gh-actions-for-hw)
- [kernel-forge](#kernel-forge)
- [agentic-asic](#agentic-asic)
- [cuda-gemm-optimization](#cuda-gemm-optimization)
- [cuda-memory-benchmark](#cuda-memory-benchmark)
- [parallel-computing-lab](#parallel-computing-lab)
- [resnet-tensorrt-bench](#resnet-tensorrt-bench)
- [triton-flash-attention-lite](#triton-flash-attention-lite)
- [lif-spiking-core](#lif-spiking-core)
- [cim-bit-serial-pe](#cim-bit-serial-pe)
- [neuro-cim-tile](#neuro-cim-tile)
- [tiny-tpu-systolic-array](#tiny-tpu-systolic-array)
- [hw-ml-tutorials](#hw-ml-tutorials)
- [rust-systems-track](#rust-systems-track)

## hw-agent-tooling

Find and choose the hardware-agent tools in this portfolio.

**Who it is for:** Engineers choosing hardware-agent tools and readers evaluating the portfolio.

**First task:** Follow the small FIFO walkthrough to see RTL review, simulation, and synthesis together.

**What to expect:** A map of the tool family, a recorded example, and links to individual tools.

**Current scope:** A documentation hub with example transcripts; each tool is installed and maintained in its own repository.

**Start here:** [FIFO walkthrough](https://github.com/zesun33/hw-agent-tooling/blob/main/examples/end-to-end-demo/README.md).

**Related projects:** [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold), [agentic-asic](https://github.com/zesun33/agentic-asic), [kernel-forge](https://github.com/zesun33/kernel-forge).

## eda-docker-images

Run open-source hardware tools in shared Docker or Podman images.

**Who it is for:** Hardware developers who need consistent EDA tools locally or in CI.

**First task:** Pull the Verilog image and run the counter fixture using the Quickstart.

**What to expect:** A containerized simulator and tool-version output; image downloads and builds may be substantial.

**Current scope:** Four EDA image definitions and smoke fixtures. Tool availability depends on the selected image and tag.

**Start here:** [Image Quickstart](https://github.com/zesun33/eda-docker-images/blob/main/README.md#quickstart).

**Related projects:** [eda-devcontainer](https://github.com/zesun33/eda-devcontainer), [gh-actions-for-hw](https://github.com/zesun33/gh-actions-for-hw), [mcp-verilog](https://github.com/zesun33/mcp-verilog).

## eda-devcontainer

Develop hardware projects in editor containers backed by EDA images.

**Who it is for:** VS Code or Cursor users developing RTL, circuits, FPGA, or ASIC designs.

**First task:** Open the Verilog profile in a development container and run its fixture checks.

**What to expect:** An editor environment backed by the EDA images, with extensions and workspace tasks.

**Current scope:** Development environments for four domains. A Docker or Podman runtime and the corresponding base image are required.

**Start here:** [Devcontainer Quickstart](https://github.com/zesun33/eda-devcontainer/blob/main/README.md#quickstart).

**Related projects:** [eda-docker-images](https://github.com/zesun33/eda-docker-images), [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold).

## mcp-verilog

Lint, compile, and simulate Verilog/SystemVerilog through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `verilog_toolchain_info` before running a design.

**What to expect:** Compiler/simulator availability, followed by diagnostics and testbench outcomes.

**Current scope:** Published MCP server. The npx command starts a stdio server that waits for a client; EDA execution also needs its documented host/container tools.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-verilog/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review), [mcp-cocotb](https://github.com/zesun33/mcp-cocotb), [eda-docker-images](https://github.com/zesun33/eda-docker-images).

## hw-agent-skills

Apply hardware-review and verification rubrics through coding-agent instruction files.

**Who it is for:** Engineers guiding a coding agent through RTL review, verification, or kernel analysis.

**First task:** Read the RTL reviewer rubric, then apply it to a clocked Verilog block.

**What to expect:** A concrete review checklist; copy or export the source files for your client.

**Current scope:** Eight instruction/rubric packs. These guide review behavior; executing EDA commands requires separate tools.

**Start here:** [RTL review rubric](https://github.com/zesun33/hw-agent-skills/blob/main/skills/rtl-reviewer/SKILL.md).

**Related projects:** [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review), [mcp-verilog](https://github.com/zesun33/mcp-verilog), [kernel-forge](https://github.com/zesun33/kernel-forge).

## hw-verification-suite

Reuse Python testbench components for LIF neuron tiles and AER routing.

**Who it is for:** Verification engineers building LIF neuron or AER router testbenches.

**First task:** Inspect the LIF scoreboard and compare its expected membrane state with your design.

**What to expect:** Reusable Python drivers, monitors, scoreboards, and stimulus/coverage utilities.

**Current scope:** Python verification components for specific interfaces. Adapting them to another design requires matching its signals and timing; quick checks skip simulation.

**Start here:** [LIF scoreboard](https://github.com/zesun33/hw-verification-suite/blob/main/hw_verification/vip/lif/lif_scoreboard.py).

**Related projects:** [lif-spiking-core](https://github.com/zesun33/lif-spiking-core), [mcp-cocotb](https://github.com/zesun33/mcp-cocotb).

## mcp-cocotb

Run Python hardware testbenches and inspect their results through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `cocotb_toolchain_info` before running a design.

**What to expect:** Simulator/tool availability, then discovered tests and parsed pass/fail results.

**Current scope:** Published MCP server. The npx command starts a stdio server that waits for a client; EDA execution also needs its documented host/container tools.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-cocotb/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-verilog](https://github.com/zesun33/mcp-verilog), [hw-verification-suite](https://github.com/zesun33/hw-verification-suite).

## mcp-yosys

Inspect synthesis, hierarchy, and unintended latches before physical design through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `yosys_toolchain_info` before running a design.

**What to expect:** Tool availability, then synthesis statistics, hierarchy, and latch diagnostics.

**Current scope:** Published MCP server. The npx command starts a stdio server that waits for a client; EDA execution also needs its documented host/container tools.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-yosys/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-verilog](https://github.com/zesun33/mcp-verilog), [mcp-openroad](https://github.com/zesun33/mcp-openroad).

## mcp-rtl-review

Review RTL assignment, width, and reset rules before simulation through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `rtl_toolchain_info` before running a design.

**What to expect:** AST-backend availability, then rule findings with source locations and a review score.

**Current scope:** Published static-analysis server using a Verilator AST backend. A review score covers the implemented rules and does not replace simulation or formal properties. The npx command waits for an MCP client.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-rtl-review/blob/main/README.md#execution-runtime).

**Related projects:** [hw-agent-skills](https://github.com/zesun33/hw-agent-skills), [mcp-verilog](https://github.com/zesun33/mcp-verilog), [mcp-formal](https://github.com/zesun33/mcp-formal).

## mcp-openroad

Run physical-design stages and inspect timing for a netlist through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `openroad_toolchain_info` before running a design.

**What to expect:** Tool availability, then placement/routing artifacts and stage-specific timing metrics.

**Current scope:** Published MCP server. The npx command starts a stdio server that waits for a client; EDA execution also needs its documented host/container tools.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-openroad/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-yosys](https://github.com/zesun33/mcp-yosys), [mcp-gds](https://github.com/zesun33/mcp-gds), [agentic-asic](https://github.com/zesun33/agentic-asic).

## mcp-gds

Inspect layouts, stream out GDS, and run geometry or netlist checks through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `gds_toolchain_info` before running a design.

**What to expect:** Tool availability, then layout summaries and check results for the chosen inputs/decks.

**Current scope:** Published MCP server for layout and netlist checks. Smoke geometry checks use the selected deck; PDK-specific extraction/LVS requires appropriate technology and setup files. The npx command waits for an MCP client.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-gds/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-openroad](https://github.com/zesun33/mcp-openroad), [agentic-asic](https://github.com/zesun33/agentic-asic).

## mcp-formal

Check assertions and run bounded or inductive RTL proofs through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `formal_toolchain_info` before running a design.

**What to expect:** Engine availability, then explicit proof, counterexample, unknown, error, or timeout results.

**Current scope:** Published MCP server with explicit proof outcomes. A proof applies to the supplied properties, assumptions, engine, and bounds; unknown or timeout is not success. The npx command waits for an MCP client.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-formal/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review), [mcp-verilog](https://github.com/zesun33/mcp-verilog).

## mcp-fpga

Synthesize and route FPGA designs and prepare bitstreams through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `fpga_toolchain_info` before running a design.

**What to expect:** Tool availability, then synthesis/place-and-route metrics and bitstream artifacts.

**Current scope:** Published MCP server for iCE40/ECP5 flows. Programming defaults to a dry run and requires an attached board for an actual hardware check. The npx command waits for an MCP client.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-fpga/blob/main/README.md#execution-runtime).

**Related projects:** [mcp-yosys](https://github.com/zesun33/mcp-yosys), [mcp-verilog](https://github.com/zesun33/mcp-verilog).

## mcp-spice

Run ngspice circuit netlists and retrieve measurement results through an MCP server.

**Who it is for:** Hardware engineers using an MCP-capable client or coding agent.

**First task:** Configure the server in your MCP client, then call `spice_toolchain_info` before running a design.

**What to expect:** Simulator availability, then parsed circuit measurements and execution status.

**Current scope:** Published MCP server. The npx command starts a stdio server that waits for a client; EDA execution also needs its documented host/container tools.

**Start here:** [Runtime requirements and configuration](https://github.com/zesun33/mcp-spice/blob/main/README.md#execution-runtime).

**Related projects:** [eda-docker-images](https://github.com/zesun33/eda-docker-images), [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold).

## hw-agent-scaffold

Create a starter RTL project and configuration for nine hardware MCP servers.

**Who it is for:** New users who want a small RTL project and the hardware MCP configuration in one step.

**First task:** Run `npx @zesun33/create-hw-agent my-asic`, inspect the generated files, then follow its README.

**What to expect:** Starter counter RTL, a testbench, a Makefile, and a client configuration for all nine MCP servers.

**Current scope:** Scaffolding is available from npm. Simulation and physical design still need a container runtime, images, and any relevant PDK.

**Start here:** [Generated project instructions](https://github.com/zesun33/hw-agent-scaffold/blob/main/template/README.md).

**Related projects:** [hw-agent-tooling](https://github.com/zesun33/hw-agent-tooling), [eda-docker-images](https://github.com/zesun33/eda-docker-images), [mcp-verilog](https://github.com/zesun33/mcp-verilog).

## gh-actions-for-hw

Run hardware checks through reusable GitHub Actions.

**Who it is for:** Repository maintainers adding hardware checks to GitHub CI.

**First task:** Copy the Verilog simulation action usage into a workflow for your RTL and testbench.

**What to expect:** A CI job that executes the selected EDA check and reports failure to GitHub.

**Current scope:** Six composite actions backed by container images. Simulation, synthesis, and physical-design checks have different inputs and prerequisites.

**Start here:** [Workflow usage](https://github.com/zesun33/gh-actions-for-hw/blob/main/README.md#usage).

**Related projects:** [eda-docker-images](https://github.com/zesun33/eda-docker-images), [mcp-verilog](https://github.com/zesun33/mcp-verilog).

## kernel-forge

Generate CUDA kernel templates and inspect correctness, timing, and modeled Roofline limits.

**Who it is for:** CUDA developers learning or automating kernel generation and performance analysis.

**First task:** Install from the checkout and run `forge doctor --json` before generating a kernel.

**What to expect:** CUDA-visible device information; generated templates can then be checked and timed on your GPU.

**Current scope:** A Python CLI with CUDA templates and modeled Roofline analysis. Actual execution requires a CUDA GPU/toolkit; modeled limits are separate from measured timings.

**Start here:** [CLI Quickstart](https://github.com/zesun33/kernel-forge/blob/main/README.md#quick-start).

**Related projects:** [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization), [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark).

## agentic-asic

Coordinate RTL review, verification, synthesis, and implementation through EDA MCP servers.

**Who it is for:** Hardware engineers combining several EDA stages into one repeatable workflow.

**First task:** Install the CLI from the checkout, run `asic doctor`, then inspect the counter demo.

**What to expect:** Per-stage results and a report tying review, verification, synthesis, and implementation together.

**Current scope:** An orchestrator over the MCP servers. Results apply to the selected design, constraints, tools, and PDK; a successful run does not establish manufacturing qualification.

**Start here:** [CLI walkthrough](https://github.com/zesun33/agentic-asic/blob/main/README.md#quick-tour--cli-usage).

**Related projects:** [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold), [mcp-openroad](https://github.com/zesun33/mcp-openroad), [mcp-gds](https://github.com/zesun33/mcp-gds).

## cuda-gemm-optimization

Compare correctness and measured FP32 throughput across naive, tiled, and cuBLAS GEMM.

**Who it is for:** Learners and GPU engineers comparing matrix-multiplication implementations.

**First task:** Read the recorded comparison, then run the checked GEMM executable on your own selected GPU.

**What to expect:** Correctness checks plus latency/throughput comparisons for naive GEMM, shared-memory tiles, and strict FP32 cuBLAS.

**Current scope:** Implemented CUDA comparison with recorded RTX A5000 measurements. Speedups depend on shape and hardware; later optimizations remain future work.

**Start here:** [Benchmark method and limitations](https://github.com/zesun33/cuda-gemm-optimization/blob/main/BENCHMARKS.md).

**Related projects:** [kernel-forge](https://github.com/zesun33/kernel-forge), [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark).

## cuda-memory-benchmark

Learn CUDA memory behavior through notes and a bandwidth exercise scaffold.

**Who it is for:** CUDA learners studying memory access and bandwidth.

**First task:** Read the memory-hierarchy notes, then implement the TODOs in the global-memory exercise.

**What to expect:** An exercise framework to turn into a correctness-checked bandwidth measurement.

**Current scope:** Notes and an incomplete CUDA exercise are present. Timing, allocation, and copy-kernel TODOs must be completed before it provides a bandwidth result.

**Start here:** [Memory-hierarchy notes](https://github.com/zesun33/cuda-memory-benchmark/blob/main/notes/00_memory_hierarchy.md).

**Related projects:** [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization), [kernel-forge](https://github.com/zesun33/kernel-forge).

## parallel-computing-lab

Learn CPU parallelism by completing OpenMP exercises.

**Who it is for:** Learners moving from serial CPU code to OpenMP parallel regions and loops.

**First task:** Read the OpenMP notes and uncomment the first exercise one section at a time.

**What to expect:** Thread output and loop-timing experiments after completing the marked sections.

**Current scope:** Two OpenMP exercises with commented-out parallel sections. Reductions, synchronization, MPI, and measured scaling studies are future work.

**Start here:** [OpenMP basics](https://github.com/zesun33/parallel-computing-lab/blob/main/notes/01_openmp_basics.md).

**Related projects:** [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization), [rust-systems-track](https://github.com/zesun33/personal-projects/tree/main/rust-systems-track).

## resnet-tensorrt-bench

Plan a future ResNet inference study comparing precision, latency, and accuracy.

**Who it is for:** Readers planning an inference-optimization study with latency and accuracy checks.

**First task:** Review the planned export, calibration, and comparison stages before choosing the first implementation.

**What to expect:** A roadmap for a future FP32/FP16/INT8 benchmark, with an initial baseline milestone.

**Current scope:** Planning documents only. Model export, engines, datasets, accuracy checks, and benchmark code are not implemented here yet.

**Start here:** [Planned implementation stages](https://github.com/zesun33/resnet-tensorrt-bench/blob/main/README.md#learning-roadmap-planned).

**Related projects:** [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization), [triton-flash-attention-lite](https://github.com/zesun33/triton-flash-attention-lite).

## triton-flash-attention-lite

Plan a future tiled-attention implementation and correctness/performance study.

**Who it is for:** Learners planning to study tiled attention and online softmax.

**First task:** Read the roadmap and define a reference attention calculation before implementing a Triton kernel.

**What to expect:** A sequence of planned baseline, softmax, tiling, and correctness/performance tasks.

**Current scope:** Planning documents only; no attention kernel or measured benchmark is present.

**Start here:** [Planned attention study](https://github.com/zesun33/triton-flash-attention-lite/blob/main/README.md#learning-roadmap-planned).

**Related projects:** [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization), [resnet-tensorrt-bench](https://github.com/zesun33/resnet-tensorrt-bench).

## lif-spiking-core

Study and simulate LIF neuron tiles, AER routing, and a 2x2 neuromorphic mesh.

**Who it is for:** RTL and neuromorphic-computing developers studying event-driven neuron tiles and routing.

**First task:** Read the architecture, then follow the neuron/tile testbench paths and verification notes.

**What to expect:** LIF neuron/tile/router RTL, reference models, simulation tests, and recorded implementation artifacts.

**Current scope:** Implemented RTL and testbenches with historical results. Coverage is partial; implementation artifacts and timing estimates are not measurements of fabricated silicon.

**Start here:** [Architecture overview](https://github.com/zesun33/lif-spiking-core/blob/main/ARCHITECTURE.md).

**Related projects:** [hw-verification-suite](https://github.com/zesun33/hw-verification-suite), [mcp-cocotb](https://github.com/zesun33/mcp-cocotb), [rust-systems-track](https://github.com/zesun33/personal-projects/tree/main/rust-systems-track).

## cim-bit-serial-pe

Specify a proposed bit-serial compute-in-memory processing element.

**Who it is for:** Hardware learners comparing bit-serial arithmetic and locally stored weights.

**First task:** Work through the activation-bit accumulation equation and the proposed interface.

**What to expect:** An architectural specification to guide a future RTL implementation and reference model.

**Current scope:** Architecture draft only: no RTL, simulation tests, measured area, or power results are present.

**Start here:** [Arithmetic and interface proposal](https://github.com/zesun33/cim-bit-serial-pe/blob/main/ARCHITECTURE.md).

**Related projects:** [tiny-tpu-systolic-array](https://github.com/zesun33/tiny-tpu-systolic-array), [neuro-cim-tile](https://github.com/zesun33/neuro-cim-tile).

## neuro-cim-tile

Specify a proposed compute-in-memory tile and its digital/device-model boundaries.

**Who it is for:** Researchers planning the boundaries between digital accumulation and CIM device models.

**First task:** Trace the proposed row-driver, crossbar, accumulator, and activation interfaces.

**What to expect:** A hierarchy/interface proposal for a future tile model and digital implementation.

**Current scope:** Architecture draft only. RTL, behavioral device models, calibration data, and verification are future work.

**Start here:** [Tile hierarchy proposal](https://github.com/zesun33/neuro-cim-tile/blob/main/ARCHITECTURE.md).

**Related projects:** [cim-bit-serial-pe](https://github.com/zesun33/cim-bit-serial-pe), [lif-spiking-core](https://github.com/zesun33/lif-spiking-core).

## tiny-tpu-systolic-array

Specify a proposed INT8 systolic-array dataflow and interface.

**Who it is for:** Hardware learners studying matrix-multiplication dataflow and PE timing.

**First task:** Trace one small matrix product through the proposed skewed input schedule.

**What to expect:** A systolic-array dataflow and interface proposal to implement and compare with a software GEMM reference.

**Current scope:** Architecture draft only: no synthesizable array, executable regression, or measured implementation is present.

**Start here:** [Systolic dataflow proposal](https://github.com/zesun33/tiny-tpu-systolic-array/blob/main/ARCHITECTURE.md).

**Related projects:** [cim-bit-serial-pe](https://github.com/zesun33/cim-bit-serial-pe), [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization).

## hw-ml-tutorials

Learn practical hardware and GPU workflows with step-by-step tutorials and runnable examples.

**Who it is for:** Learners and engineers who want concrete examples connecting the portfolio tools.

**First task:** Run the event-counter positive and negative tests, then follow the MCP workflow lesson.

**What to expect:** Passing functional checks, an intentional failure, JSON EDA reports, and optional GPU/model exercises.

**Current scope:** Eight lessons and runnable hardware fixtures, a university resource library, a Windows setup guide, and an initial GCD course specification. The new ASIC course implementations are upcoming work; GPU measurements require actual CUDA hardware.

**Start here:** [First simulation tutorial](https://github.com/zesun33/hw-ml-tutorials/blob/main/lessons/01-first-simulation.md).

**Related projects:** [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold), [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review), [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization), [kernel-forge](https://github.com/zesun33/kernel-forge), [lif-spiking-core](https://github.com/zesun33/lif-spiking-core).

## rust-systems-track

Follow private Rust fundamentals toward planned GEMM and LIF/AER systems projects.

**Who it is for:** The maintainer following the Rust curriculum and readers interested in its future systems projects.

**First task:** Use the plan and tracker to understand the sequence and phase exit criteria.

**What to expect:** Public curriculum metadata for private Rust fundamentals, followed by planned GEMM and LIF/AER projects.

**Current scope:** Basics remain private. The public systems bridge and golden-model repositories are future phases, not released tools.

**Start here:** [Curriculum and exit criteria](https://github.com/zesun33/personal-projects/blob/main/rust-systems-track/PLAN.md).

**Related projects:** [parallel-computing-lab](https://github.com/zesun33/parallel-computing-lab), [lif-spiking-core](https://github.com/zesun33/lif-spiking-core).
