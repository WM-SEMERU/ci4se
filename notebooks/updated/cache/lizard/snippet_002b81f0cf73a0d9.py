def wait(self, timeout=None):
    try:
        if timeout:
            gevent.sleep(timeout)
        else:
            while True:
                gevent.sleep(1000)
    except (KeyboardInterrupt, SystemExit, Exception):
        pass