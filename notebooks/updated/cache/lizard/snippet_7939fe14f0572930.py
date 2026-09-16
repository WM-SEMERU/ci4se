def run(self):
    self.start()
    timeout = self._stop_flag_timeout
    health_check_ts = time.time()
    while True:
        try:
            self.stop_flag.wait(timeout=timeout)
        except KeyboardInterrupt:
            self._logger.info('Received SIGINT')
            self.stop(graceful=True)
        except:
            self._logger.exception('Error in consumer.')
            self.stop()
        else:
            if self._received_signal:
                self.stop(graceful=self._graceful)
        if self.stop_flag.is_set():
            break
        if self._health_check:
            now = time.time()
            if now >= health_check_ts + self._health_check_interval:
                health_check_ts = now
                self.check_worker_health()
    if self._restart:
        self._logger.info('Consumer will restart.')
        python = sys.executable
        os.execl(python, python, *sys.argv)
    else:
        self._logger.info('Consumer exiting.')