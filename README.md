# Hardware Acceleration & ML Systems Portfolio

A learning-focused portfolio demonstrating mastery of the AI Hardware Stack: CUDA, Memory Systems, Parallel Computing, and Production Deployment.

## 📊 Skills Coverage Matrix

| Skill | Project(s) | Status |
|-------|-----------|--------|
| **CUDA Kernels** | cuda-gemm-optimization, cuda-memory-benchmark | ✅ Active |
| **Memory Systems** | cuda-memory-benchmark | ✅ Active |
| **Quantization (INT8/FP16)** | resnet-tensorrt-bench | ⬜ Planned |
| **OpenMP/MPI** | parallel-computing-lab | ✅ Active |
| **TensorRT** | resnet-tensorrt-bench | ⬜ Planned |
| **Triton Compiler** | triton-flash-attention-lite | ⬜ Planned |

---

## 🚀 Core Portfolio Projects

### 1. [Foundation] CUDA GEMM Optimization
**Status**: 🔄 In Progress | [GitHub](https://github.com/zesun33/cuda-gemm-optimization)

Learn GPU kernel optimization from naive to highly optimized:
- ✅ Naive GEMM (baseline)
- ⬜ Global Memory Coalescing
- ⬜ Shared Memory Tiling
- ⬜ Vectorized Loads (float4)
- ⬜ Tensor Core (WMMA)

**Target**: Achieve >80% of cuBLAS performance.

---

### 2. [Memory] CUDA Memory Benchmark ⭐ NEW
**Status**: 🔄 In Progress | [GitHub](https://github.com/zesun33/cuda-memory-benchmark)

Understand GPU memory hierarchy and optimization:
- ✅ Memory hierarchy theory (5 notes)
- ✅ Bandwidth theory & roofline model
- ✅ Coalescing patterns & bank conflicts
- ⬜ Implement bandwidth benchmarks

**Relevance**: Critical for Micron-style memory systems roles.

---

### 3. [Parallel] Parallel Computing Lab ⭐ NEW
**Status**: 🔄 In Progress | [GitHub](https://github.com/zesun33/parallel-computing-lab)

Master CPU parallel programming:
- ✅ Parallel computing concepts (2 notes)
- ✅ OpenMP basics
- ✅ Hello parallel & parallel_for examples
- ⬜ Reduction, GEMM OpenMP
- ⬜ MPI basics (future)

**Relevance**: Covers OpenMP/MPI from Micron preferred qualifications.

---

### 4. [Deployment] TensorRT Quantization Benchmark
**Status**: ⬜ Planned | [GitHub](https://github.com/zesun33/resnet-tensorrt-bench)

Production inference optimization:
- ⬜ ONNX export from PyTorch
- ⬜ TensorRT engine building
- ⬜ FP32 → FP16 → INT8 comparison
- ⬜ INT8 calibration

**Prerequisite**: Requires TensorRT SDK installation.

---

### 5. [Compiler] FlashAttention Lite (Triton)
**Status**: ⬜ Planned | [GitHub](https://github.com/zesun33/triton-flash-attention-lite)

Modern GPU kernel development:
- ⬜ Triton basics
- ⬜ FlashAttention algorithm
- ⬜ Block-level memory management

---

## 📖 Learning Philosophy

**Theory First, Code Second**: Each project has a `notes/` directory with:
1. Theory and fundamentals
2. Step-by-step explanations
3. Study questions and exercises
4. References

**Incremental Implementation**: Code files include:
- `TODO` sections to complete
- Expected results for verification
- Exercises for deeper understanding

---

## 🎯 Industry Relevance

| Target Role | Key Projects |
|-------------|-------------|
| **Micron ML Engineering** | cuda-memory-benchmark, parallel-computing-lab |
| **NVIDIA/GPU Engineering** | All CUDA projects, triton-flash-attention |
| **ML Infrastructure** | resnet-tensorrt-bench, cuda-gemm-optimization |
| **HPC/Cloud** | parallel-computing-lab, cuda-memory-benchmark |

---

## 🔧 Prerequisites

- **CUDA Toolkit**: For all CUDA projects
- **GCC with OpenMP**: `g++ -fopenmp` (included with GCC ✅)
- **TensorRT SDK**: For resnet-tensorrt-bench (optional)
- **Triton**: `pip install triton` (optional)
- **NVIDIA GPU**: For running CUDA code

---

## 📚 Recommended Learning Order

1. **cuda-memory-benchmark** (notes) — Understand memory hierarchy
2. **parallel-computing-lab/openmp** — Learn parallel patterns
3. **cuda-gemm-optimization** — Apply memory concepts to GEMM
4. **resnet-tensorrt-bench** — Production deployment
5. **triton-flash-attention-lite** — Modern compiler development

---

## 📈 Progress Tracking

**Last Updated**: January 2026

| Project | Notes | Code | Verified |
|---------|-------|------|----------|
| cuda-gemm-optimization | 4/7 | 1/5 | ✅ Naive |
| cuda-memory-benchmark | 5/5 | 1/5 | ⬜ |
| parallel-computing-lab | 2/4 | 2/5 | ⬜ |
| resnet-tensorrt-bench | 0/4 | 0/5 | ⬜ |
| triton-flash-attention-lite | 0/3 | 0/4 | ⬜ |

---

## 🔗 All Repository Links

| Project | GitHub | Description |
|---------|--------|-------------|
| cuda-gemm-optimization | [Link](https://github.com/zesun33/cuda-gemm-optimization) | GEMM optimization from naive to Tensor Cores |
| cuda-memory-benchmark | [Link](https://github.com/zesun33/cuda-memory-benchmark) | GPU memory hierarchy and bandwidth |
| parallel-computing-lab | [Link](https://github.com/zesun33/parallel-computing-lab) | OpenMP/MPI parallel computing |
| resnet-tensorrt-bench | [Link](https://github.com/zesun33/resnet-tensorrt-bench) | TensorRT quantization (FP32/FP16/INT8) |
| triton-flash-attention-lite | [Link](https://github.com/zesun33/triton-flash-attention-lite) | FlashAttention with Triton compiler |
