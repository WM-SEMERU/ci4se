def _init_num_threads():
    if 'sparc' in platform.machine():
        log.warning(
            'The number of threads have been set to 1 because problems related to threading have been reported on some sparc machine. The number of threads can be changed using the "set_num_threads" function.'
            )
        set_num_threads(1)
        return 1
    env_configured = False
    n_cores = detect_number_of_cores()
    if 'NUMEXPR_MAX_THREADS' in os.environ:
        env_configured = True
        n_cores = MAX_THREADS
    else:
        if n_cores > MAX_THREADS:
            log.info(
                'Note: detected %d virtual cores but NumExpr set to maximum of %d, check "NUMEXPR_MAX_THREADS" environment variable.'
                 % (n_cores, MAX_THREADS))
        if n_cores > 8:
            log.info(
                'Note: NumExpr detected %d cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 8.'
                 % n_cores)
            n_cores = 8
    if 'NUMEXPR_NUM_THREADS' in os.environ:
        requested_threads = int(os.environ['NUMEXPR_NUM_THREADS'])
    elif 'OMP_NUM_THREADS' in os.environ:
        requested_threads = int(os.environ['OMP_NUM_THREADS'])
    else:
        requested_threads = n_cores
        if not env_configured:
            log.info('NumExpr defaulting to %d threads.' % n_cores)
    set_num_threads(requested_threads)
    return requested_threads