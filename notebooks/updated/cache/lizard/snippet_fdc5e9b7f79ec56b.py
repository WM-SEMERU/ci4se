def discover(name, wait_for_s=60):
    _start_beacon()
    t0 = time.time()
    while True:
        discovery = _rpc('discover', name, 0.5)
        if discovery:
            return discovery
        if timed_out(t0, wait_for_s):
            return None