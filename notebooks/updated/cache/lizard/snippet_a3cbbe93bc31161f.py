def enable_parallel_lz4(mode):
    global ENABLE_PARALLEL
    ENABLE_PARALLEL = bool(mode)
    logger.info('Setting parallelisation mode to {}'.format(
        'multi-threaded' if mode else 'single-threaded'))