def set_rtscts(self, enable):
    try:
        self.port.setRtsCts(enable)
    except Exception:
        self.port.rtscts = enable
    self.rtscts = enable