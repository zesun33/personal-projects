#!/usr/bin/env python3
"""Export public portfolio metadata to the separate Jekyll website checkout."""
import argparse
import json
from pathlib import Path
from catalog import ROOT, FAMILIES, load_catalog, project_url

FEATURED = ['hw-agent-scaffold', 'cuda-gemm-optimization', 'lif-spiking-core',
            'kernel-forge', 'agentic-asic', 'hw-agent-tooling']


def document(data):
    projects = []
    for project in data['projects']:
        row = dict(project)
        row['url'] = project_url(project)
        row['featured'] = project['path'] in FEATURED
        if project['path'] == 'hw-ml-tutorials':
            label = 'Guided examples'
        elif project['path'] == 'lif-spiking-core':
            label = 'Implemented RTL; partial coverage'
        elif project['path'] == 'cuda-gemm-optimization':
            label = 'Measured experiment'
        elif project['status'] == 'active':
            label = 'Learning exercise'
        elif project['status'] == 'planned':
            label = 'Architecture draft' if project['kind'] == 'architecture' else 'Roadmap'
        elif project['status'] == 'learning':
            label = 'Curriculum metadata; basics private'
        else:
            label = 'Usable tool'
        row['status_label'] = label
        row['start_url'] = ((project['github'] + '/blob/main/' if project['github'] else
                             data['catalog_repository'] + '/blob/main/' + project['path'] + '/')
                            + project['guide']['start_file'])
        projects.append(row)
    return json.dumps({
        'catalog_url': data['catalog_repository'],
        'guide_url': data['catalog_repository'] + '/blob/main/PROJECT_GUIDE.md',
        'getting_started_url': data['catalog_repository'] + '/blob/main/GETTING_STARTED.md',
        'featured': FEATURED,
        'groups': [{'id': key, 'title': title} for key, title in FAMILIES.items()],
        'projects': projects,
    }, indent=2, ensure_ascii=False) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--website', type=Path, default=ROOT.parent / 'personal-website')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    target = args.website / '_data' / 'portfolio.json'
    if not (args.website / '_config.yml').is_file() or not target.parent.is_dir():
        parser.error('--website must point to the existing Jekyll website checkout')
    data = load_catalog()
    repos = ['github_users:', '  - zesun33', '', 'repo_description_lines_max: 2', '',
             '# Exported from the personal-projects catalog; see DEVELOPMENT.md.',
             'github_repos:', '  - zesun33/personal-projects']
    repos += ['  - zesun33/' + p['path'] for p in data['projects'] if p['github']]
    repos += ['  - zesun33/zesun33.github.io', '']
    outputs = {target: document(data), target.parent / 'repositories.yml': '\n'.join(repos)}
    for path, content in outputs.items():
        if args.check:
            same = path.is_file() and (json.loads(path.read_text()) == json.loads(content)
                                      if path.suffix == '.json' else path.read_text() == content)
            if not same:
                print('Website catalog needs refresh: python3 scripts/export_website.py')
                return 1
        else:
            path.write_text(content)
    print('Website catalog consistent' if args.check else
          'Exported ' + str(len(data['projects'])) + ' project entries to ' + str(target.parent))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
