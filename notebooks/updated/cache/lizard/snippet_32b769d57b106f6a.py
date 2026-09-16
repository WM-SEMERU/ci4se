def run_hive_script(script):
    if not os.path.isfile(script):
        raise RuntimeError('Hive script: {0} does not exist.'.format(script))
    return run_hive(['-f', script])