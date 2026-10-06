"""Shared catalog loading, generated files, and Git URL comparison (Python 3.9+)."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAMILIES = {'hw-agent': 'Hardware agent tooling', 'ml-systems': 'ML systems',
            'silicon': 'Silicon designs', 'tutorials': 'Practical tutorials', 'rust': 'Rust systems'}


def load_catalog(root=ROOT):
    data = json.loads((root / 'projects.json').read_text())
    if data['schema_version'] != 1:
        raise ValueError('Unsupported catalog schema_version')
    names = set()
    for project in data['projects']:
        name = project['path']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name in names:
            raise ValueError(f'Invalid or duplicate project path: {name}')
        names.add(name)
        if project['family'] not in FAMILIES:
            raise ValueError(f'{name}: unknown family')
        if project['status'] not in {'shipped', 'active', 'planned', 'learning'}:
            raise ValueError(f'{name}: unknown status')
        if project['github'] not in (None, f'https://github.com/zesun33/{name}'):
            raise ValueError(f'{name}: unexpected GitHub URL')
        steps = project.get('verify_steps', [])
        if bool(steps) != (project['verification'] == 'available'):
            raise ValueError(f'{name}: verification availability mismatch')
        for step in steps:
            if not isinstance(step, list) or not step or any(not isinstance(arg, str) or not arg for arg in step):
                raise ValueError(f'{name}: verification steps must be argument lists')
        if project.get('npm_package') and not isinstance(project.get('npm_published'), bool):
            raise ValueError(f'{name}: specify npm publication status')
        guide = project.get('guide', {})
        for field in ['audience', 'first_task', 'outcome', 'scope', 'start_file', 'start_label']:
            if not isinstance(guide.get(field), str) or not guide[field].strip():
                raise ValueError(f'{name}: missing guide {field}')
        start = Path(guide['start_file'].split('#', 1)[0])
        if start.is_absolute() or '..' in start.parts:
            raise ValueError(f'{name}: guide start_file must stay within the repository')
        if not isinstance(guide.get('related'), list):
            raise ValueError(f'{name}: guide related projects must be a list')
    for profile, paths in data['profiles'].items():
        if not re.fullmatch(r'[a-z0-9-]+', profile) or len(paths) != len(set(paths)) or not set(paths) <= names:
            raise ValueError(f'Invalid workspace profile: {profile}')
    for project in data['projects']:
        if not set(project['guide']['related']) <= names:
            raise ValueError(project['path'] + ': unknown related project')
    return data


def normalize_git_url(url):
    url = url.removeprefix('git+')
    if url.startswith('git@github.com:'):
        url = 'https://github.com/' + url.split(':', 1)[1]
    if url.startswith('ssh://git@github.com/'):
        url = 'https://github.com/' + url.split('github.com/', 1)[1]
    return url.rstrip('/').removesuffix('.git')


def generated_files(data):
    projects = data['projects']
    names = [project['path'] for project in projects]
    files = {}
    profiles = {'personal-projects': names, **data['profiles']}
    for profile, selected in profiles.items():
        workspace = {
            'folders': [{'name': 'personal-projects', 'path': '.'}] +
                       [{'name': name, 'path': name} for name in selected],
            'settings': {**data['workspace_settings'],
                         'files.exclude': {name: True for name in names}},
            'extensions': {'recommendations': data['workspace_extensions']},
        }
        files[profile + '.code-workspace'] = json.dumps(workspace, indent=2) + '\n'
    files['STATUS.md'] = status_document(data)
    files['PROJECT_GUIDE.md'] = project_guide(data)
    return files


GUIDE_START = '<!-- BEGIN GENERATED PROJECT GUIDE -->'
GUIDE_END = '<!-- END GENERATED PROJECT GUIDE -->'


def project_url(project):
    return project['github'] or ('https://github.com/zesun33/personal-projects/tree/main/' + project['path'])


def orientation(project, data, repository_readme=False):
    guide = project['guide']
    by_name = {p['path']: p for p in data['projects']}
    base = (project['github'] + '/blob/main/' if project['github'] else
            'https://github.com/zesun33/personal-projects/blob/main/' + project['path'] + '/')
    start = guide['start_file'] if repository_readme else base + guide['start_file']
    lines = [project['description'] + '.', '',
             '**Who it is for:** ' + guide['audience'], '',
             '**First task:** ' + guide['first_task'], '',
             '**What to expect:** ' + guide['outcome'], '',
             '**Current scope:** ' + guide['scope'], '',
             f"**Start here:** [{guide['start_label']}]({start})."]
    if guide['related']:
        links = [f'[{name}]({project_url(by_name[name])})' for name in guide['related']]
        lines += ['', '**Related projects:** ' + ', '.join(links) + '.']
    return '\n'.join(lines)


def readme_orientation(project, data):
    return '\n'.join([GUIDE_START, '', '## Purpose and first steps', '',
                      orientation(project, data, repository_readme=True), '',
                      '[Choose another project](https://github.com/zesun33/personal-projects/blob/main/GETTING_STARTED.md).',
                      GUIDE_END])


def project_guide(data):
    lines = ['# Project guide', '',
             'Choose a starting route in [GETTING_STARTED.md](GETTING_STARTED.md). This reference explains the audience, first task, result, and current scope of every catalog project.', '',
             'Generated from `projects.json`; project README introductions use the same metadata.', '',
             '## Index', '']
    lines += [f"- [{p['path']}](#{p['path']})" for p in data['projects']]
    for p in data['projects']:
        lines += ['', '## ' + p['path'], '', orientation(p, data)]
    return '\n'.join(lines) + '\n'


def status_document(data):
    lines = ['# Portfolio status', '',
             'Generated from `projects.json` by `python3 scripts/generate_catalog.py`.', '',
             'Maturity reflects the repository roadmap. It is not a fresh test result, silicon fabrication claim, or physical signoff verdict.', '',
             '| Family | Shipped | Active | Planned | Learning |', '|---|---:|---:|---:|---:|']
    for family, label in FAMILIES.items():
        group = [p for p in data['projects'] if p['family'] == family]
        counts = [sum(p['status'] == s for p in group) for s in ['shipped', 'active', 'planned', 'learning']]
        lines.append('| ' + label + ' | ' + ' | '.join(map(str, counts)) + ' |')
    lines += ['', '| Project | Status | Verification entry point | Next milestone |', '|---|---|---|---|']
    for p in data['projects']:
        command = ' → '.join('`' + ' '.join(step) + '`' for step in p.get('verify_steps', []))
        link = p['github'] or p['path'] + '/README.md'
        lines.append(f"| [{p['path']}]({link}) | {p['status']} | {command or p['verification'].replace('_', ' ')} | {p['next_milestone']} |")
    return '\n'.join(lines) + '\n'


def ignore_block(data):
    lines = ['# BEGIN GENERATED PROJECT CHECKOUTS']
    lines += [f"/{p['path']}/" for p in data['projects'] if p['github']]
    lines.append('# END GENERATED PROJECT CHECKOUTS')
    return '\n'.join(lines)


def readme_block(data):
    lines = ['<!-- BEGIN GENERATED PROJECT CATALOG -->']
    for family, label in FAMILIES.items():
        lines += ['', '## ' + label, '', '| Project | Purpose | Maturity | Distribution |', '|---|---|---|---|']
        for p in data['projects']:
            if p['family'] != family:
                continue
            link = p['github'] or p['path'] + '/README.md'
            distribution = 'GitHub source' if p['github'] else 'Catalog metadata; basics private'
            if p.get('npm_published'):
                distribution = f"[npm](https://www.npmjs.com/package/{p['npm_package']})"
            elif p.get('npm_package'):
                distribution = 'Source files (no npm package)'
            lines.append(f"| [{p['path']}]({link}) | {p['description']} | {p['status']} | {distribution} |")
    lines += ['', 'Rust path: private Phase 0 basics → future public `rust-quant-gemm` → future public `lif-rust-golden` co-checked against `lif-spiking-core`. See [PLAN](rust-systems-track/PLAN.md) and [TRACKER](rust-systems-track/TRACKER.md). Private drill solutions are never cataloged as public projects.', '', '<!-- END GENERATED PROJECT CATALOG -->']
    return '\n'.join(lines)


def replace_block(text, block, start, end):
    before, separator, rest = text.partition(start)
    if not separator or end not in rest:
        raise ValueError(f'Missing generated markers: {start}')
    after = rest.partition(end)[2]
    return before + block + after
