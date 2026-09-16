def suppress_interrupt():
    interrupted = False

    def sigint_handler(signum, frame):
        nonlocal interrupted
        interrupted = True
    s = signal.signal(signal.SIGINT, sigint_handler)
    try:
        yield None
    finally:
        signal.signal(signal.SIGINT, s)
    if interrupted:
        raise KeyboardInterrupt()