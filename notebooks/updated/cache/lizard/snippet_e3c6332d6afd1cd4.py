def graceful_exit(servers, *, loop, signals=frozenset({signal.SIGINT,
    signal.SIGTERM})):
    signals = set(signals)
    flag = []
    for sig_num in signals:
        loop.add_signal_handler(sig_num, _exit_handler, sig_num, servers, flag)
    try:
        yield
    finally:
        for sig_num in signals:
            loop.remove_signal_handler(sig_num)