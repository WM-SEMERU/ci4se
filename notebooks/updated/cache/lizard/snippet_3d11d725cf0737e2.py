def run_in_twisted(self, url=DEFAULT_AUTOBAHN_ROUTER, realm=
    DEFAULT_AUTOBAHN_REALM, authmethods=None, authid=None, authrole=None,
    authextra=None, callback=None, **kwargs):
    _init_crochet(in_twisted=True)
    logger.debug('run_in_crossbar, bootstraping')
    blocking = callback is None

    def bootstrap_and_callback():
        self._bootstrap(blocking, url=url, realm=realm, authmethods=
            authmethods, authid=authid, authrole=authrole, authextra=
            authextra, **kwargs)
        if callback:
            callback()
        self._callbacks_runner.start()
    threads.deferToThread(bootstrap_and_callback)