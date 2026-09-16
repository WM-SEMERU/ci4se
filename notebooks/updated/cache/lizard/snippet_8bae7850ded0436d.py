def stop_sync(self):
    if self.connected:
        self.disconnect_sync(self._connection_handle)
    self.set_advertising(False)
    self.bable.stop()
    self.actions.queue.clear()