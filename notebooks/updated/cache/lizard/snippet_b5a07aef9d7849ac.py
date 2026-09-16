def env_same_host(env1, env2):
    config = _config_file()
    h1 = dict(config.items(env1))['base_url']
    h2 = dict(config.items(env2))['base_url']
    return h1 == h2