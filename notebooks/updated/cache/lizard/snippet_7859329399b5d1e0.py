def _check_env(fn):

    def decorator(*args, **kwargs):
        resultdir = kwargs.get('--env', SYMLINK_NAME)
        env_path = os.path.join(resultdir, 'env')
        if not os.path.isfile(env_path):
            raise Exception('The file %s does not exist.' % env_path)
        return fn(*args, **kwargs)
    return decorator