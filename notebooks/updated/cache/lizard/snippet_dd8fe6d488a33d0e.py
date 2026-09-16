def restart_on_change_helper(lambda_f, restart_map, stopstart=False,
    restart_functions=None):
    if restart_functions is None:
        restart_functions = {}
    checksums = {path: path_hash(path) for path in restart_map}
    r = lambda_f()
    restarts = [restart_map[path] for path in restart_map if path_hash(path
        ) != checksums[path]]
    services_list = list(OrderedDict.fromkeys(itertools.chain(*restarts)))
    if services_list:
        actions = ('stop', 'start') if stopstart else ('restart',)
        for service_name in services_list:
            if service_name in restart_functions:
                restart_functions[service_name](service_name)
            else:
                for action in actions:
                    service(action, service_name)
    return r