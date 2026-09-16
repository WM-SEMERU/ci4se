def __start(self):
    assert not self._listener_thread
    self._listener_thread = threading.Thread(target=self.__run_listener,
        name='clearly-listener')
    self._listener_thread.daemon = True
    self._listener_thread.start()
    self._wait_event.wait()
    self._wait_event.clear()