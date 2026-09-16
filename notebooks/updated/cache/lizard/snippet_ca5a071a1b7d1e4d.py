def set(self):
    self._flag = True
    old_future = self._waiting_future
    self._waiting_future = tornado_Future()
    old_future.set_result(True)