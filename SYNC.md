# Using this portfolio on another machine

`personal-projects` tracks the catalog, focused workspace files, status, and scripts. Its 27 child repositories keep separate Git histories. Pulling the parent updates organization files; child code is updated separately.

## Existing checkout

In the other machine's `personal-projects` directory:

```bash
git status --short
git pull --ff-only
python3 scripts/check_catalog.py --catalog-only
python3 scripts/sync_projects.py --clone-missing --pull --dry-run
python3 scripts/sync_projects.py --clone-missing --pull
python3 scripts/check_catalog.py --network
```

Inspect the dry-run before applying. The sync helper refuses dirty child checkouts, unexpected remotes, symlink checkout paths, non-main branches, and unpublished local commits. It uses fast-forward pulls and never resets, stashes, deletes files, or pushes. Blocked repositories stay untouched; other repositories can still update, and the script returns failure if any need attention. Commit or otherwise resolve local changes yourself before trying again.

The parent `git pull` must also have a clean worktree and a compatible branch. A sync transfers committed/pushed files; it does not transfer uncommitted work from this machine.

## Fresh checkout

```bash
git clone https://github.com/zesun33/personal-projects.git
cd personal-projects
python3 scripts/check_catalog.py --catalog-only
python3 scripts/sync_projects.py --clone-missing
python3 scripts/check_catalog.py
```

All checkout/workspace paths are relative. You can place this directory anywhere. Python 3.9+ and Git are required by the catalog scripts. Node/npm, EDA containers, GPU tools, and other runtime dependencies are installed separately when needed.

## Working on one area

Open `hardware-agent.code-workspace`, `silicon-designs.code-workspace`, `ml-systems.code-workspace`, or `rust-track.code-workspace`. To clone/pull only one catalog family, add `--family hw-agent`, `--family silicon`, `--family ml-systems`, or `--family rust` to the sync helper. Shared tools may appear in several workspaces; each still has only one checkout.

## npm and npx

GitHub source and npm releases are separate distributions. A Git pull updates source; npx runs the published package version. `hw-agent-skills` is a public source repository with `private: true` in its package manifest to prevent accidental npm publishing; this does not make its GitHub repository private.

```bash
python3 scripts/check_catalog.py --network
python3 scripts/check_npm.py
npx -y @zesun33/create-hw-agent my-asic
```

The registry check compares latest published versions, executable mappings, and GitHub links with local package metadata. The npx check pins each package to the version in the local manifest, exercises MCP `tools/list`, and creates a temporary scaffold. It does not run EDA commands. Changes to local scaffold code reach npx users only after a separate npm release.

## Verification coverage

```bash
./scripts/verify_portfolio_full.sh --list
./scripts/verify_portfolio_full.sh --project hw-agent-scaffold
./scripts/verify_portfolio_full.sh --family hw-agent
CUDA_ARCH=sm_86 ./scripts/verify_portfolio_full.sh --include-gpu --project cuda-gemm-optimization
```

The compatibility shell script reads commands from `projects.json`. No GPU index is hard-coded; set `CUDA_VISIBLE_DEVICES` if needed. The CUDA architecture defaults to that project's Makefile unless `CUDA_ARCH` is set. Missing automated suites and opt-out GPU checks are shown separately from passes. Each run stores logs in a new temporary directory.

EDA suites can require container images, installed Python packages, and a PDK; container builds and hardware-dependent tests can take time. See each repository's verification script for its actual prerequisites.

### Known runtime incompatibility observed on 2026-10-01

The available `ghcr.io/zesun33/verilog` image contains Verilator 5.050. `mcp-rtl-review` still requests `--xml-only`, which that version rejects. Its full local suite has six integration failures; passing unit tests and npm startup do not establish working AST review. Supporting the new Verilator AST format is separate functional work. Use a separately verified XML-capable image for that server, or repair the AST backend before treating it as verified. Do not downgrade the shared image without checking cocotb compatibility.

## Updating organization

Edit `projects.json`, then regenerate and validate:

```bash
python3 scripts/generate_catalog.py
python3 scripts/check_catalog.py
python3 -m unittest discover -s tests
```

Generated files: workspace profiles, `STATUS.md`, README project tables, and the marked checkout section of `.gitignore`. Other README/ignore content stays handwritten. CI checks the generated output and scripts without requiring child clones. Project-specific README, npm metadata, code, and tests remain owned by each child repository.
