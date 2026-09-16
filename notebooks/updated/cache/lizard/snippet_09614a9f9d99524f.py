def _write(self, data):
    frame = APIFrame(data, self._escaped).output()
    self.serial.write(frame)