def _get_registry_auth(registry_url, config_path):
    username = None
    password = None
    try:
        docker_config = json.load(open(config_path))
    except ValueError:
        return username, password
    if docker_config.get('auths'):
        docker_config = docker_config['auths']
    auth_key = docker_config.get(registry_url, {}).get('auth', None)
    if auth_key:
        username, password = base64.b64decode(auth_key).split(':', 1)
    return username, password