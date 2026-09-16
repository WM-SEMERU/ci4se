def query_build_version(config, log):
    url = '/projects/{0}/{1}/history?recordsNumber=10'.format(config[
        'owner'], config['repo'])
    log.debug('Querying AppVeyor history API for %s/%s...', config['owner'],
        config['repo'])
    json_data = query_api(url)
    if 'builds' not in json_data:
        log.error('Bad JSON reply: "builds" key missing.')
        raise HandledError
    for build in json_data['builds']:
        if config['tag'] and config['tag'] == build.get('tag'):
            log.debug('This is a tag build.')
        elif config['pull_request'] and config['pull_request'] == build.get(
            'pullRequestId'):
            log.debug('This is a pull request build.')
        elif config['commit'] == build['commitId']:
            log.debug('This is a branch build.')
        else:
            continue
        log.debug('Build JSON dict: %s', str(build))
        return build['version']
    return None