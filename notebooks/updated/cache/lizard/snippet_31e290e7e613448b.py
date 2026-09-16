def print_dependencies(_run):
    print('Dependencies:')
    for dep in _run.experiment_info['dependencies']:
        pack, _, version = dep.partition('==')
        print('  {:<20} == {}'.format(pack, version))
    print('\nSources:')
    for source, digest in _run.experiment_info['sources']:
        print('  {:<43}  {}'.format(source, digest))
    if _run.experiment_info['repositories']:
        repos = _run.experiment_info['repositories']
        print('\nVersion Control:')
        for repo in repos:
            mod = COLOR_DIRTY + 'M' if repo['dirty'] else ' '
            print('{} {:<43}  {}'.format(mod, repo['url'], repo['commit']) +
                ENDC)
    print('')