def validate_monitor_tasks(dependencies, args):
    sup_configs = sorted(dependencies.keys())
    try:
        logging.info('Validating supervisor data...')
        r = fapi.list_workspace_configs(args['project'], args['workspace'])
        fapi._check_response_code(r, 200)
        space_configs = r.json()
        space_configs = {c['name']: c for c in space_configs}
        r = fapi.list_repository_methods()
        fapi._check_response_code(r, 200)
        repo_methods = r.json()
        repo_methods = {(m['namespace'] + '/' + m['name'] + ':' + str(m[
            'snapshotId'])) for m in repo_methods if m['entityType'] ==
            'Workflow'}
        valid = True
        for config in sup_configs:
            if config not in space_configs:
                logging.error('No task configuration for ' + config +
                    ' found in ' + args['project'] + '/' + args['workspace'])
                valid = False
            else:
                m = space_configs[config]['methodRepoMethod']
                ref_method = m['methodNamespace'] + '/' + m['methodName'
                    ] + ':' + str(m['methodVersion'])
                if ref_method not in repo_methods:
                    logging.error(config +
                        " -- You don't have permisson to run the referenced method: "
                         + ref_method)
                    valid = False
    except Exception as e:
        logging.error('Exception occurred while validating supervisor: ' +
            str(e))
        raise
        return False
    return valid