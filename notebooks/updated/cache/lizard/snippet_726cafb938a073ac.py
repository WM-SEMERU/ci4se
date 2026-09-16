def ci_data(namespace, name, branch='master'):
    with repository(namespace, name, branch) as (path, latest, cache):
        if not path or not latest:
            return {'build_success': NOT_FOUND, 'status': NOT_FOUND}
        elif latest in cache:
            return json.loads(cache[latest])
    starting = {'status': 'starting'}
    cache[latest] = json.dumps(starting)
    ci_worker(namespace, name, branch=branch, _bg=True)
    return starting