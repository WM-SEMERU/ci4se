def load_env():
    for key, envvar in [['cache_dir', 'INTAKE_CACHE_DIR'], ['catalog_path',
        'INTAKE_PATH'], ['persist_path', 'INTAKE_PERSIST_PATH']]:
        if envvar in os.environ:
            conf[key] = make_path_posix(os.environ[envvar])
    conf['catalog_path'] = intake_path_dirs(conf['catalog_path'])
    for key, envvar in [['cache_disabled', 'INTAKE_DISABLE_CACHING'], [
        'cache_download_progress', 'INTAKE_CACHE_PROGRESS']]:
        if envvar in os.environ:
            conf[key] = os.environ[envvar].lower() in ['true', 't', 'y', 'yes']
    if 'INTAKE_LOG_LEVEL' in os.environ:
        conf['logging'] = os.environ['INTAKE_LOG_LEVEL']