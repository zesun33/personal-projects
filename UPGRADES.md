# Technical upgrades — 2026-10-03

The repositories remain independent. Pull this catalog and use the dry-run-first child synchronization commands in [SYNC.md](SYNC.md).

## kernel-forge 0.1.1

GPU discovery and execution use CUDA-visible ordinals. The default is visible GPU 0; `--device` overrides local `FORGE_DEVICE`. CUDA resolves reordered and UUID masks. Optional host GPU IDs are metadata only. Invalid selections fail instead of silently choosing another GPU. Keep shared-cluster device policy in your shell, for example `CUDA_VISIBLE_DEVICES=4`, rather than in public source defaults.

Python distributions include all three CUDA templates. Templates validate their complete outputs, and the Python runner rejects failed/missing correctness validation and invalid timing samples. Roofline traffic and bottlenecks are explicitly modeled estimates. The Python package is distributed through GitHub source/release assets; it is not an npm package.

The tested wheel and source archive are available in the [kernel-forge 0.1.1 release](https://github.com/zesun33/kernel-forge/releases/tag/v0.1.1).

Validation: 14 portable unit tests, all six verification gates with live vector-add/tiled-GEMM execution, reordered device-mask/local-preference checks, no-GPU quick checks, and an isolated wheel install with template generation and CUDA execution.

## CUDA GEMM optimization

The new comparison measures naive GEMM, shared-memory tiles of 16 and 32, and strict FP32 cuBLAS on identical seeded inputs. Scalar, rectangular, odd-sized, and square cases are checked with independent CPU sums and full-output cuBLAS comparisons. Invalid dimensions and iteration counts fail.

The recorded RTX A5000 run includes raw timing samples, correctness errors, hardware/toolchain metadata, source/executable hashes, CSV, and a chart. At 1024³, tiled16 measured 1.29× naive throughput and cuBLAS 8.31×; small cases show different tradeoffs. See [method and limitations](https://github.com/zesun33/cuda-gemm-optimization/blob/main/BENCHMARKS.md) and [results](https://github.com/zesun33/cuda-gemm-optimization/blob/main/results/2026-10-03-rtx-a5000/results.json).

The portfolio runner treats both GPU projects as opt-in. To execute their full checks on a chosen host GPU:

```bash
CUDA_VISIBLE_DEVICES=4 ./scripts/verify_portfolio_full.sh --include-gpu --project kernel-forge
CUDA_VISIBLE_DEVICES=4 CUDA_ARCH=sm_86 ./scripts/verify_portfolio_full.sh --include-gpu --project cuda-gemm-optimization
```

## LIF hardware evidence

The documentation labels recorded simulation outcomes, partial coverage, implementation artifacts, and timing-derived Fmax separately. It retains historical numerical tables and explains that their raw timing reports/tool manifests are not tracked. Quick verification checks RTL elaboration, documentation, and artifact presence; it does not rerun timing, DRC, LVS, or the historical 18-test suite. Skipped simulation gates are reported as skipped. Missing simulation prerequisites cannot produce a successful simulation gate.

## npm distribution and release automation

All nine published MCP servers and the scaffold were exercised through npx. These Python/CUDA/hardware-documentation changes do not require republishing unrelated npm packages. `@zesun33/mcp-rtl-review@0.2.2` remains the published runtime release.

The RTL-review repository now includes a GitHub Actions release workflow with a default dry run, exact version checks, build/unit verification, isolated tarball smoke test, artifact upload, optional OIDC publication, and registry integrity verification. See [RELEASING.md](https://github.com/zesun33/mcp-rtl-review/blob/main/RELEASING.md). An npm account trusted-publisher configuration is required before enabling actual OIDC publication; a successful dry run is not proof of that authorization.

The [GitHub release-workflow dry run](https://github.com/zesun33/mcp-rtl-review/actions/runs/37134334664) passed on the final workflow revision. It built and checked the package, installed the tarball in isolation, verified the MCP version and six registered tools, and uploaded the release artifact. Publication and registry verification were skipped because `publish=false`.

The same release process now covers all ten published npm packages, each in its own repository. The nine added workflows passed local build/unit checks and isolated tarball installation/registration or scaffold generation. See [NPM_RELEASES.md](NPM_RELEASES.md) for the catalog-driven batch trusted-publisher helper. It inspects existing settings, creates only missing repository-specific publishers, and verifies each result. npm account configuration is still unverified; browser approval is required before applying the batch.

All ten release workflows and normal CI checks also passed on GitHub with publication disabled. Exact commits and dry-run links are recorded in [NPM_RELEASES.md](NPM_RELEASES.md#verified-dry-runs--2026-10-04).
