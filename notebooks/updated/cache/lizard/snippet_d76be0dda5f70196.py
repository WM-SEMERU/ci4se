def timeout(delay, handler=None):
    delay = int(delay)
    if handler is None:

        def default_handler(signum, frame):
            raise RuntimeError('{:d} seconds timeout expired'.format(delay))
        handler = default_handler
    prev_sigalrm_handler = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(delay)
    yield
    signal.alarm(0)
    signal.signal(signal.SIGALRM, prev_sigalrm_handler)