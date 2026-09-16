def env_valid(env):
    if env not in EFConfig.ENV_LIST:
        raise ValueError('unknown env: {}; env must be one of: '.format(env
            ) + ', '.join(EFConfig.ENV_LIST))
    return True