def id(self):
    dev_id = ''
    if self._is_x10:
        dev_id = 'x10{}{:02d}'.format(self.x10_housecode, self.x10_unitcode)
    else:
        dev_id = self.hex
    return dev_id