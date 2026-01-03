# Hardware Acceleration & ML Systems Portfolio

This repository collection demonstrates a complete mastery of the "AI Hardware Stack," from low-level kernel optimization to modern compiler infrastructure and production deployment.

## Strategic Goal: The "Lucrative" Switch
This portfolio is engineered to bridge the gap between **Academic Research** (PhD/SciPy/PyTorch) and **Production AI Engineering** (C++/CUDA/Compilers).

The goal is to demonstrate "Vertical Integration": the rare ability to not just *design* a model (Research), but to *scale* and *optimize* it for hardware (Systems). This skill set is critical for top-tier teams at NVIDIA, Meta (PyTorch Team), Google (XLA/TPU), and Microsoft (ONNX).

---

## 1. Core Portfolio Projects (The "Trifecta")

These three projects were selected to cover the distinct layers of the modern AI stack.

### [Foundation] CUDA GEMM Optimization
*   **Repo**: [`cuda-gemm-optimization`](./cuda-gemm-optimization)
*   **The Industry "Why"**:
    *   **CUDA** is the "Assembly Language" of modern AI. Knowing it distinguishes you from 99% of ML practitioners who only know Python.
    *   **GEMM (General Matrix Multiply)** is the atomic unit of Deep Learning (90%+ of FLOPs in LLMs).
*   **Implementation Plan**:
    *   Start with a naive C++ kernel.
    *   Implement **Global Memory Coalescing** to maximize bandwidth.
    *   Use **Shared Memory Tiling** to minimize latency (the "classic" GPU interview question).
    *   Finalize with **Tensor Core (WMMA)** instructions to unlock FP16 peak performance.
*   **Target**: Achieve >80% of `cuBLAS` performance.

### [Compiler] FlashAttention Lite (Triton)
*   **Repo**: [`triton-flash-attention-lite`](./triton-flash-attention-lite)
*   **The Industry "Why"**:
    *   **OpenAI Triton** is the "Disruptor." It allows writing GPU kernels in Python-like syntax.
    *   Major labs (Meta, OpenAI) are actively rewriting their fastest kernels in Triton. It is a "Unicorn Skill."
*   **Implementation Plan**:
    *   Re-implement the **FlashAttention** algorithm (tiling Q, K, V blocks in SRAM) to reduce HBM reads.
    *   Focus on **Block-level Memory Management** rather than thread-level (CUDA).
*   **Target**: Write a 100-line kernel that outperforms standard PyTorch Attention on long sequences (N > 4096).

### [Deployment] ResNet "Speed Run" (TensorRT)
*   **Repo**: [`resnet-tensorrt-bench`](./resnet-tensorrt-bench)
*   **The Industry "Why"**:
    *   **TensorRT** is the "Closer." It is what runs inside self-driving cars, robots, and real-time clouds.
    *   The industry needs engineers who understand **Quantization** (FP16/INT8) and trade-offs between throughput and latency.
*   **Implementation Plan**:
    *   Export a standard ResNet50/ViT to **ONNX**.
    *   Build a **TensorRT Engine** with explicit FP16 refinement.
    *   Profile **Latency (ms)** vs **Throughput (img/sec)**.

---

## 2. Open Source Contribution Strategy

Beyond this portfolio, I am actively targeting contributions to high-impact open-source repositories to prove "Production Readiness."

*   **SpikingJelly (SNNs)**: Targeting Issue #576 (STDPLearner Memory Leak). Fixing a memory leak proves ability to profile and debug complex research code.
*   **Hugging Face Transformers**: Targeting Issue #28103 (SDPA Support for OWL-VIT). Adding Scaled Dot Product Attention proves knowledge of modern PyTorch optimization.
*   **TorchAO (Architecture Optimization)**: Targeting FP8 Benchmarking (Issue #2713), aligning with the industry shift to low-precision training on H100s.

## Future Roadmap
*   **SNN Optimization**: Implementing custom CUDA kernels for LIF neuron updates.
*   **LLM Serving**: Integrating PagedAttention (vLLM style) into the Triton kernel.
