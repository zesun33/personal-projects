# Start with a goal

This portfolio connects algorithm performance, hardware design, and tools for testing both. You can use one repository independently or follow a route across related projects. Start with one small result, then choose the next stage from its README.

Follow the separate [hardware and ML tutorial project](https://github.com/zesun33/hw-ml-tutorials) for eight consecutive lessons, runnable examples, deliberate failures, and troubleshooting.

## Choose a route

| Goal | First repository | What you need | What to try next |
|---|---|---|---|
| Run a small hardware simulation with the agent tools | [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold) | Node/npm and Podman for the generated simulation Makefile | Review the RTL with [mcp-rtl-review](https://github.com/zesun33/mcp-rtl-review) and synthesize with [mcp-yosys](https://github.com/zesun33/mcp-yosys) |
| Use one EDA capability from an agent/client | [Individual MCP servers](PROJECT_GUIDE.md#mcp-verilog) | An MCP client, Node/npm, and that server's runtime prerequisites | Add only the servers needed for your design |
| Measure GPU GEMM performance | [cuda-gemm-optimization](https://github.com/zesun33/cuda-gemm-optimization) | A CUDA GPU, compiler, and cuBLAS | Inspect [kernel-forge](https://github.com/zesun33/kernel-forge) for generation and modeled Roofline analysis |
| Learn memory and CPU parallelism | [cuda-memory-benchmark](https://github.com/zesun33/cuda-memory-benchmark), [parallel-computing-lab](https://github.com/zesun33/parallel-computing-lab) | CUDA for the memory exercise; GCC/OpenMP for the CPU exercises | Complete the marked TODOs before interpreting results as benchmarks |
| Study a hardware implementation | [lif-spiking-core](https://github.com/zesun33/lif-spiking-core) | RTL-reading basics; simulator and Python dependencies for tests | Explore [hw-verification-suite](https://github.com/zesun33/hw-verification-suite) and the reference models |
| Discuss or implement a proposed architecture | [CIM and systolic drafts](PROJECT_GUIDE.md#cim-bit-serial-pe) | The architecture document and a software reference for the intended arithmetic | Define correctness criteria, then implement the first small RTL block |
| Plan future attention or inference work | [Triton attention](https://github.com/zesun33/triton-flash-attention-lite), [TensorRT inference](https://github.com/zesun33/resnet-tensorrt-bench) | No runtime needed to read the current plans | Implement and check a baseline before making performance claims |

The complete [project guide](PROJECT_GUIDE.md) includes every repository's audience, first task, expected result, and current scope.

## First hardware result: simulate a counter

Node/npm runs the scaffold. The generated Makefile uses **Podman** and downloads the Verilog image; the remaining EDA images are needed only for the corresponding later flows.

```bash
npx -y @zesun33/create-hw-agent doctor
npx -y @zesun33/create-hw-agent my-asic
cd my-asic
make sim
```

The generated project contains `rtl/counter.v`, `tb/counter_tb.v`, `.cursor/mcp.json`, and a Makefile. `make sim` compiles the two Verilog files and executes the self-checking testbench. Read its output and exit status before moving on to synthesis. Consult the [scaffold README](https://github.com/zesun33/hw-agent-scaffold) for container/image setup if Podman is unavailable.

Open the generated MCP configuration in a compatible client to use the nine servers. The simulation Makefile itself runs the tools directly; an agent is optional for this first check.

## Understand the pieces of the hardware stack

| Piece | Role | Repository |
|---|---|---|
| Runtime | Provides the EDA executables inside containers | [eda-docker-images](https://github.com/zesun33/eda-docker-images) |
| Editor environment | Opens your code with the runtime and editor tooling | [eda-devcontainer](https://github.com/zesun33/eda-devcontainer) |
| Agent guidance | Supplies engineering review/test rubrics | [hw-agent-skills](https://github.com/zesun33/hw-agent-skills) |
| MCP servers | Expose individual EDA operations to a client | [Nine servers in the project guide](PROJECT_GUIDE.md#mcp-verilog) |
| Starter project | Creates files and a server configuration | [hw-agent-scaffold](https://github.com/zesun33/hw-agent-scaffold) |
| Orchestration | Coordinates several EDA stages and collects results | [agentic-asic](https://github.com/zesun33/agentic-asic) |
| CI | Runs selected checks on GitHub | [gh-actions-for-hw](https://github.com/zesun33/gh-actions-for-hw) |

An **MCP server** waits for a client to send tool requests over its input/output stream. Running `npx -y @zesun33/mcp-verilog` in a terminal starts that server; it does not present an interactive design CLI. Use the client configuration in that server's README, then request its toolchain probe before running a design.

Keep file paths, top-module names, testbench names, and clock constraints explicit. FPGA programming also needs a physical board; ASIC extraction and technology-specific checks need the appropriate PDK files.

## Read results with their scope

| Repository type | What it gives you today | How to judge it |
|---|---|---|
| Usable tool | Code, installation instructions, fixtures, and checks | Try the small documented case and inspect its result |
| Measured experiment | Code plus recorded samples and methodology | Check correctness, hardware, shape, and measurement conditions |
| Learning exercise | Notes and code containing TODOs | Finish the exercise and add a correctness check before benchmarking |
| Architecture draft | A proposed arithmetic/dataflow/interface specification | Review the assumptions; implementation and verification are next milestones |
| Roadmap | An intended study with no current implementation | Discuss scope and establish a baseline before investing in a runtime setup |

The GEMM repository includes recorded performance data. The memory and OpenMP repositories contain exercises. The three CIM/systolic repositories currently contain architecture documents. TensorRT and Triton attention are roadmap stubs. LIF has RTL, tests, and implementation artifacts, with separate notes about historical results and partial coverage.

For your own learning, keep the next concrete task visible. For other users, show the input, expected output, prerequisites, and evidence behind a claim. Useful contribution requests include the project/version, the small input that reproduces a problem, the command or tool request, and the actual result.

## A few terms used throughout

| Term | Meaning in this portfolio |
|---|---|
| RTL | Register-transfer-level code describing digital hardware |
| EDA | Electronic design automation: tools for simulation, synthesis, implementation, and checks |
| MCP | Model Context Protocol: a client/server interface for tool requests |
| GEMM | General matrix multiplication, used as a core performance workload |
| Roofline | A model comparing computation with data movement to reason about performance limits |
| LIF / AER | Leaky integrate-and-fire neurons / address-event representation of spikes |
| CIM | Compute-in-memory: architectures that keep arithmetic close to stored weights |
| PDK | Process design kit containing technology-specific models and implementation/checking files |
| STA / DRC / LVS | Static timing analysis / design-rule checking / layout-versus-schematic comparison |

See [DEPENDENCIES.md](DEPENDENCIES.md) for relationships and [SYNC.md](SYNC.md) for a local multi-repository checkout. Pulling the catalog alone does not pull the child code.
