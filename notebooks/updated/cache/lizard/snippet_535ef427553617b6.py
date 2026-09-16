def install_signal_handlers(self):
    self.graceful_stop = False

    def request_shutdown_now():
        self.shutdown_now()

    def request_shutdown_graceful():
        if self.graceful_stop:
            self.shutdown_now()
        else:
            self.graceful_stop = True
            self.shutdown_graceful()
    gevent.signal(signal.SIGINT, request_shutdown_graceful)
    gevent.signal(signal.SIGTERM, request_shutdown_now)