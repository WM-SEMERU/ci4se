def close(self):
    if self.pyb and self.pyb.serial:
        self.pyb.serial.close()
    self.pyb = None