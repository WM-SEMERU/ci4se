def stop(self):
    if self.is_alive():
        self._proc.terminate()
    if self._proc is not None:
        self.__cleanup()
        if self.raise_error:
            if self._proc.exitcode == 255:
                raise LoopExceptionError(
                    'the loop function return non zero exticode ({})!\n'.
                    format(self._proc.exitcode) +
                    'see log (INFO level) for traceback information')
    self.pipe_handler.close()
    self._proc = None