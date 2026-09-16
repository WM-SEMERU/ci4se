def _FlushInput(self):
    self.ser.flush()
    flushed = 0
    while True:
        ready_r, ready_w, ready_x = select.select([self.ser], [], [self.ser], 0
            )
        if len(ready_x) > 0:
            logging.error('Exception from serial port.')
            return None
        elif len(ready_r) > 0:
            flushed += 1
            self.ser.read(1)
            self.ser.flush()
        else:
            break