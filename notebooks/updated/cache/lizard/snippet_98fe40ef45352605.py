def _create_process(self, process, name):

    def _run():
        process.initialize()
        try:
            while not self.stop_flag.is_set():
                process.loop()
        except KeyboardInterrupt:
            pass
        except:
            self._logger.exception('Process %s died!', name)
    return self.environment.create_process(_run, name)