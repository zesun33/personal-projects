# npm releases across the portfolio

The ten published npm packages each keep their own GitHub repository, package version, and `publish.yml` workflow. Other projects and unpublished packages are excluded. The release workflows default to dry runs and publish only when explicitly dispatched with `publish=true` after verification.

## Batch trusted-publisher setup

Use npm 11.15.0 or newer, Node 22.14.0 or newer, GitHub CLI authentication, npm package write access, and account 2FA. First synchronize the parent and child repositories following [SYNC.md](SYNC.md).

Preview the exact package/repository mappings without network requests:

```bash
python3 scripts/setup_npm_trust.py
```

Run this in your own interactive terminal so you can immediately approve npm's browser verification:

```bash
npm login --auth-type=web --browser=false --registry=https://registry.npmjs.org
python3 scripts/setup_npm_trust.py --apply
```

On the first trust verification page, select npm's option to skip further 2FA for five minutes. The helper waits two seconds between registry calls. npm's [bulk setup instructions](https://docs.npmjs.com/cli/v11/commands/npm-trust/#bulk-usage) document this temporary window; it does not remove account 2FA. Keep passwords and OTPs on npm's page.

The helper checks package/catalog mappings and the live workflow on GitHub before changing settings. It inspects all selected packages before creating missing trust, preserves exact existing matches, and stops on conflicting settings or authorization errors. It verifies every created configuration. A failed batch can be rerun; it never revokes trust, publishes packages, or changes versions.

```bash
python3 scripts/setup_npm_trust.py --check
python3 scripts/setup_npm_trust.py --apply --project mcp-rtl-review
```

`--check` only reads account settings and exits unsuccessfully if any configuration is missing. Browser approval can still be required for inspection. Trusted publishers use repository-specific GitHub identities, `publish.yml`, no environment restriction, and direct publication permission. There is no account-wide wildcard publisher.

## Each package release

1. Update that repository's package version, lockfile where present, and release notes. Run its full local verification when runtime code changes, including any EDA integration checks.
2. Commit and push to `main`; wait for CI. Each repository stays independent.
3. Dispatch `publish.yml` with the exact version and `publish=false`. Inspect the tested tarball artifact.
4. After trusted publishing has been verified, dispatch again with the same version and `publish=true`. The workflow builds, tests, checks an isolated tarball installation, publishes through OIDC, and verifies registry integrity.
5. Check a fresh registry installation and create a matching GitHub release.

For example:

```bash
gh workflow run publish.yml --repo zesun33/mcp-verilog --ref main -f version=0.2.1 -f publish=false
```

An existing npm version cannot be overwritten. A dry run verifies packaging and command/MCP registration; it does not prove account authorization, actual publication, or EDA runtime behavior. Account configuration remains unverified until the batch's `--check` or `--apply` completes successfully.

## Verified dry runs — 2026-10-04

All ten GitHub release dry runs and their normal CI checks passed on the commits below. Each dry run used `publish=false`: no npm versions were created and npm account authorization was not exercised. The tarball artifacts are attached to these runs.

| Repository | Version | Source commit | Successful release dry run |
|---|---|---|---|
| mcp-verilog | 0.2.1 | [`3d1199b`](https://github.com/zesun33/mcp-verilog/commit/3d1199b7f2bfbc2bb1273f5837fbadf86d6ba745) | [run 37248378389](https://github.com/zesun33/mcp-verilog/actions/runs/37248378389) |
| mcp-cocotb | 0.2.2 | [`3adcf22`](https://github.com/zesun33/mcp-cocotb/commit/3adcf22f5769be9b8470c35ac27bd44fac5499ce) | [run 37248382889](https://github.com/zesun33/mcp-cocotb/actions/runs/37248382889) |
| mcp-yosys | 0.2.1 | [`09df588`](https://github.com/zesun33/mcp-yosys/commit/09df58822fc9844a9e1745b7efce94171e73d66e) | [run 37248387706](https://github.com/zesun33/mcp-yosys/actions/runs/37248387706) |
| mcp-rtl-review | 0.2.2 | [`cc7841f`](https://github.com/zesun33/mcp-rtl-review/commit/cc7841f5a729ec8496cfddd7a3de177c92615c80) | [run 37248392549](https://github.com/zesun33/mcp-rtl-review/actions/runs/37248392549) |
| mcp-openroad | 0.2.4 | [`2a87694`](https://github.com/zesun33/mcp-openroad/commit/2a87694d6a744306ef7882f20aec91666286f398) | [run 37248398080](https://github.com/zesun33/mcp-openroad/actions/runs/37248398080) |
| mcp-gds | 0.1.2 | [`fc5eefd`](https://github.com/zesun33/mcp-gds/commit/fc5eefd5c213093d858e5e0336cdafcec8ff666f) | [run 37248403319](https://github.com/zesun33/mcp-gds/actions/runs/37248403319) |
| mcp-formal | 0.1.1 | [`47426ef`](https://github.com/zesun33/mcp-formal/commit/47426ef89a41e72b9bda79155b0d1d71d0ed24ca) | [run 37248408273](https://github.com/zesun33/mcp-formal/actions/runs/37248408273) |
| mcp-fpga | 0.1.2 | [`ad07ff3`](https://github.com/zesun33/mcp-fpga/commit/ad07ff3804b54792824d19601fcdcaa59460e3fa) | [run 37248413285](https://github.com/zesun33/mcp-fpga/actions/runs/37248413285) |
| mcp-spice | 0.1.1 | [`1a0041e`](https://github.com/zesun33/mcp-spice/commit/1a0041e0a236ea0e3b89e7408a8398bc1c72e6df) | [run 37248418104](https://github.com/zesun33/mcp-spice/actions/runs/37248418104) |
| hw-agent-scaffold | 0.1.2 | [`ea84423`](https://github.com/zesun33/hw-agent-scaffold/commit/ea84423725c428ca80dfaebbbde1eb4688fb5275) | [run 37248422620](https://github.com/zesun33/hw-agent-scaffold/actions/runs/37248422620) |
