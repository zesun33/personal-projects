# Hardware Acceleration & ML Systems Portfolio

A learning-focused portfolio demonstrating mastery of the AI Hardware Stack: CUDA, Memory Systems, Parallel Computing, and Production Deployment.

## 📊 Skills Coverage Matrix

| Skill | Project(s) | Status |
|-------|-----------|--------|
| **CUDA Kernels** | cuda-gemm-optimization, cuda-memory-benchmark | ✅ Active |
| **Memory Systems** | cuda-memory-benchmark | ✅ Active |
| **Quantization (INT8/FP16)** | resnet-tensorrt-bench | 🔄 Planned |
| **OpenMP/MPI** | parallel-computing-lab | ✅ Active |
| **TensorRT** | resnet-tensorrt-bench | 🔄 Planned |
| **Triton Compiler** | triton-flash-attention-lite | 🔄 Planned |

---

## 🚀 Core Portfolio Projects

### 1. [Foundation] CUDA GEMM Optimization
**Status**: 🔄 In Progress  
**Path**: [`cuda-gemm-optimization/`](./cuda-gemm-optimization)

Learn GPU kernel optimization from naive to highly optimized:
- ⬜ Naive GEMM (baseline) ← **Current**
- ⬜ Global Memory Coalescing
- ⬜ Shared Memory Tiling
- ⬜ Vectorized Loads (float4)
- ⬜ Tensor Core (WMMA)

**Target**: Achieve >80% of cuBLAS performance.

---

### 2. [Memory] CUDA Memory Benchmark ⭐ NEW
**Status**: 🔄 In Progress  
**Path**: [`cuda-memory-benchmark/`](./cuda-memory-benchmark)

Understand GPU memory hierarchy and optimization:
- ✅ Memory hierarchy theory
- ✅ Bandwidth theory & roofline model
- ✅ Coalescing patterns
- ✅ Bank conflicts
- ⬜ Implement bandwidth benchmarks

**Relevance**: Critical for Micron-style memory systems roles.

---

### 3. [Parallel] Parallel Computing Lab ⭐ NEW
**Status**: 🔄 In Progress  
**Path**: [`parallel-computing-lab/`](./parallel-computing-lab)

Master CPU parallel programming:
- ✅ Parallel computing concepts
- ✅ OpenMP basics
- ⬜ OpenMP examples (hello, parallel_for, reduction)
- ⬜ MPI basics (future)
- ⬜ Hybrid OpenMP+MPI (future)

**Relevance**: Covers OpenMP/MPI from Micron preferred qualifications.

---

### 4. [Deployment] TensorRT Quantization Benchmark
**Status**: ⬜ Skeleton  
**Path**: [`resnet-tensorrt-bench/`](./resnet-tensorrt-bench)

Production inference optimization:
- ⬜ ONNX export from PyTorch
- ⬜ TensorRT engine building
- ⬜ FP32 → FP16 → INT8 comparison
- ⬜ Calibration for INT8

**Prerequisite**: Requires TensorRT SDK installation.

---

### 5. [Compiler] FlashAttention Lite (Triton)
**Status**: ⬜ Skeleton  
**Path**: [`triton-flash-attention-lite/`](./triton-flash-attention-lite)

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
- **GCC with OpenMP**: `g++ -fopenmp` (included with GCC)
- **TensorRT SDK**: For resnet-tensorrt-bench (optional)
- **NVIDIA GPU**: For running CUDA code

---

## 📚 Learning Order (Recommended)

1. **Start**: `cuda-memory-benchmark` (notes only) — Understand memory hierarchy
2. **Then**: `parallel-computing-lab/openmp` — Learn parallel patterns
3. **Then**: Complete `cuda-gemm-optimization` — Apply memory concepts
4. **Later**: TensorRT and Triton projects

---

## 📈 Progress Tracking

Last Updated: January 2026

| Project | Notes | Code | Verified |
|---------|-------|------|----------|
| cuda-gemm-optimization | 4/7 | 1/5 | ✅ Naive |
| cuda-memory-benchmark | 5/5 | 0/5 | ⬜ |
| parallel-computing-lab | 2/4 | 2/5 | ⬜ |
| resnet-tensorrt-bench | 0/3 | 0/4 | ⬜ |
| triton-flash-attention-lite | 0/3 | 0/2 | ⬜ |
