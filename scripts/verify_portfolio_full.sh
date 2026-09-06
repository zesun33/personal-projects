#!/usr/bin/env bash
# verify_portfolio_full.sh — Master testing & verification scorecard runner
# Executes multi-tier verification suites across all portfolio repositories.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${ROOT_DIR}"

declare -a REPOS=(
  "hw-agent-tooling:Catalog & Standard:./scripts/verify.sh --quick"
  "mcp-verilog:MCP RTL Layer:./scripts/verify.sh"
  "hw-agent-skills:Cognitive Rubrics:./scripts/verify.sh"
  "mcp-cocotb:Python Co-Sim Layer:./scripts/verify.sh"
  "mcp-yosys:RTL Synthesis Layer:./scripts/verify.sh"
  "mcp-rtl-review:AST Review Layer:./scripts/verify.sh"
  "mcp-openroad:OpenROAD P&R Layer:./scripts/verify.sh"
  "kernel-forge:GPU Kernel Engine:./scripts/verify.sh"
  "agentic-asic:Autonomous ASIC Flow:./scripts/verify.sh"
  "hw-verification-suite:Centralized VIP:./scripts/verify.sh"
  "lif-spiking-core:SNN Tapeout Mesh:./scripts/verify.sh"
)

declare -a RESULTS=()
TOTAL_START=$(date +%s)
FAILED_COUNT=0

printf "\n\033[1;36m========================================================================\033[0m\n"
printf "\033[1;36m       Starting Full Portfolio Verification & Testing Campaign         \033[0m\n"
printf "\033[1;36m========================================================================\033[0m\n\n"

for entry in "${REPOS[@]}"; do
  IFS=":" read -r repo role cmd <<< "${entry}"
  printf "\033[1m[%s]\033[0m Running %s...\n" "${repo}" "${cmd}"
  START_TS=$(date +%s%N)
  
  if (cd "${ROOT_DIR}/${repo}" && eval "${cmd}") > /tmp/verify_${repo}.log 2>&1; then
    END_TS=$(date +%s%N)
    DURATION=$(awk "BEGIN {printf \"%.2f\", (${END_TS} - ${START_TS}) / 1000000000}")
    RESULTS+=("${repo}|${role}|${DURATION}s|PASS")
    printf "  \033[1;32m✓ PASSED\033[0m in %ss\n\n" "${DURATION}"
  else
    END_TS=$(date +%s%N)
    DURATION=$(awk "BEGIN {printf \"%.2f\", (${END_TS} - ${START_TS}) / 1000000000}")
    RESULTS+=("${repo}|${role}|${DURATION}s|FAIL")
    printf "  \033[1;31m✗ FAILED\033[0m in %ss (See /tmp/verify_%s.log)\n\n" "${DURATION}" "${repo}"
    FAILED_COUNT=$((FAILED_COUNT + 1))
  fi
done

# Native CUDA / C++ Build Smoke
printf "\033[1m[cuda-gemm-optimization]\033[0m Running sm_86 build & verify...\n"
START_TS=$(date +%s%N)
if (cd "${ROOT_DIR}/cuda-gemm-optimization" && make clean && make all && CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-4}" ./build/01_naive_gemm 512 512 512 && make clean) > /tmp/verify_gemm.log 2>&1; then
  END_TS=$(date +%s%N)
  DURATION=$(awk "BEGIN {printf \"%.2f\", (${END_TS} - ${START_TS}) / 1000000000}")
  RESULTS+=("cuda-gemm-optimization|CUDA sm_86 GEMM|${DURATION}s|PASS")
  printf "  \033[1;32m✓ PASSED\033[0m in %ss\n\n" "${DURATION}"
else
  END_TS=$(date +%s%N)
  DURATION=$(awk "BEGIN {printf \"%.2f\", (${END_TS} - ${START_TS}) / 1000000000}")
  RESULTS+=("cuda-gemm-optimization|CUDA sm_86 GEMM|${DURATION}s|FAIL")
  FAILED_COUNT=$((FAILED_COUNT + 1))
fi

TOTAL_END=$(date +%s)
TOTAL_ELAPSED=$((TOTAL_END - TOTAL_START))

# Output Scorecard Table
printf "\n\033[1;36m==============================================================================\033[0m\n"
printf "\033[1;36m                  Personal-Projects Full Portfolio Test Matrix                \033[0m\n"
printf "\033[1;36m==============================================================================\033[0m\n"
printf "  %-24s %-25s %-12s %-8s\n" "Repository" "Role in Architecture" "Duration" "Status"
printf "  ----------------------------------------------------------------------------\n"

for r in "${RESULTS[@]}"; do
  IFS="|" read -r name role dur stat <<< "${r}"
  if [ "${stat}" = "PASS" ]; then
    STAT_COLOR="\033[1;32mPASS\033[0m"
  else
    STAT_COLOR="\033[1;31mFAIL\033[0m"
  fi
  printf "  %-24s %-25s %-12s " "${name}" "${role}" "${dur}"
  echo -e "${STAT_COLOR}"
done

printf "  ----------------------------------------------------------------------------\n"
printf "  Total execution time: %d seconds\n" "${TOTAL_ELAPSED}"

if [ "${FAILED_COUNT}" -eq 0 ]; then
  printf "  \033[1;32m✔ OVERALL VERDICT: ALL %d REPOSITORIES PASSED 100%% (0 FAILURES)\033[0m\n" "${#RESULTS[@]}"
  printf "\033[1;36m==============================================================================\033[0m\n\n"
  exit 0
else
  printf "  \033[1;31m✖ OVERALL VERDICT: %d REPOSITORY FAILURES DETECTED\033[0m\n" "${FAILED_COUNT}"
  printf "\033[1;36m==============================================================================\033[0m\n\n"
  exit 1
fi
