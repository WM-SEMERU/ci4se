def loop(self, callback=None, daemonize=False, **args):
    if daemonize:
        self.__daemonize(**args)
    while 1:
        try:
            self.process_events()
            if callback is not None and callback(self) is True:
                break
            ref_time = time.time()
            if self.check_events():
                self._sleep(ref_time)
                self.read_events()
        except KeyboardInterrupt:
            log.debug('Pyinotify stops monitoring.')
            break
    self.stop()