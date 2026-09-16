def stop(self):
    if not self.is_alive():
        return
    self._shutdown_event.set()
    self.join()
    itm = self._session.target.get_first_child_of_type(ITM)
    itm.disable()
    self._session.target.trace_stop()