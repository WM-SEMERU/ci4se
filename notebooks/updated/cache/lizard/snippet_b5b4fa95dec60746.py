def __load(file_name):
    if os.path.exists(file_name) and not os.path.isfile(file_name):
        raise RuntimeError(
            'Cache should be initialized with valid full file name')
    if not os.path.exists(file_name):
        open(file_name, 'w+b').close()
        return {}
    cache_file_obj = open(file_name, 'rb')
    try:
        file_cache_t.logger.info('Loading cache file "%s".', file_name)
        start_time = timeit.default_timer()
        cache = pickle.load(cache_file_obj)
        file_cache_t.logger.debug('Cache file has been loaded in %.1f secs',
            timeit.default_timer() - start_time)
        file_cache_t.logger.debug('Found cache in file: [%s]  entries: %s',
            file_name, len(list(cache.keys())))
    except (pickle.UnpicklingError, AttributeError, EOFError, ImportError,
        IndexError) as error:
        file_cache_t.logger.exception(
            'Error occurred while reading cache file: %s', error)
        cache_file_obj.close()
        file_cache_t.logger.info('Invalid cache file: [%s]  Regenerating.',
            file_name)
        open(file_name, 'w+b').close()
        cache = {}
    finally:
        cache_file_obj.close()
    return cache