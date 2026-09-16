def prep_shell_environment(nova_env, nova_creds):
    new_env = {}
    for key, value in prep_nova_creds(nova_env, nova_creds):
        if type(value) == six.binary_type:
            value = value.decode()
        new_env[key] = value
    return new_env