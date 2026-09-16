def read_config(source, current_name):
    log = logging.getLogger(__name__)
    queue = multiprocessing.Queue()
    config = Config.from_context()
    with TempDir() as temp_dir:
        argv = 'sphinx-build', source, temp_dir
        log.debug('Running sphinx-build for config values with args: %s',
            str(argv))
        child = multiprocessing.Process(target=_read_config, args=(argv,
            config, current_name, queue))
        child.start()
        child.join()
        if child.exitcode != 0:
            log.error(
                'sphinx-build failed for branch/tag while reading config: %s',
                current_name)
            raise HandledError
    config = queue.get()
    return config