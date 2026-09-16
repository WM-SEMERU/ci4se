def disconnect(self):
    self.target_device.disconnect()
    self.ctrl.disconnect()
    self.tail_disconnect(-1)