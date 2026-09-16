def blocking_request(self, msg, timeout=None, use_mid=None):
    assert get_thread_ident(
        ) != self.ioloop_thread_id, 'Cannot call blocking_request() in ioloop'
    if timeout is None:
        timeout = self._request_timeout
    f = Future()
    tf = [None]

    def blocking_request_callback():
        try:
            tf[0] = frf = self.future_request(msg, timeout=timeout, use_mid
                =use_mid)
        except Exception:
            tf[0] = frf = tornado_Future()
            frf.set_exc_info(sys.exc_info())
        gen.chain_future(frf, f)
    self.ioloop.add_callback(blocking_request_callback)
    extra_wait = 1
    wait_timeout = timeout
    if wait_timeout is not None:
        wait_timeout = wait_timeout + extra_wait
    try:
        return f.result(timeout=wait_timeout)
    except TimeoutError:
        raise RuntimeError(
            'Unexpected error: Async request handler did not call reply handler within timeout period'
            )
    except Exception:
        tf[0].result()
        assert False