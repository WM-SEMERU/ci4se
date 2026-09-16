def wrapped_target(target, q_stdout, q_stderr, q_error, robust, name, *args,
    **kwargs):
    import sys
    sys.stdout = IOQueue(q_stdout)
    sys.stderr = IOQueue(q_stderr)
    try:
        target(*args, **kwargs)
    except:
        if not robust:
            s = 'Error in tab\n' + traceback.format_exc()
            logger = daiquiri.getLogger(name)
            logger.error(s)
        else:
            raise
        if not robust:
            q_error.put(name)
        raise