def print_logs(query, types=None):
    if query is None:
        return
    for run, log in query:
        print('{0} @ {1} - {2} id: {3} group: {4} status: {5}'.format(run.
            end, run.experiment_name, run.project_name, run.
            experiment_group, run.run_group, log.status))
        print('command: {0}'.format(run.command))
        if 'stderr' in types:
            print('StdErr:')
            print(log.stderr)
        if 'stdout' in types:
            print('StdOut:')
            print(log.stdout)
        print()