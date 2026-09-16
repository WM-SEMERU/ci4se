def __write_to_character_device(self, event_list, timeval=None):
    pos = self._character_device.tell()
    self._character_device.seek(0, 2)
    for event in event_list:
        self._character_device.write(event)
    sync = self.create_event_object('Sync', 0, 0, timeval)
    self._character_device.write(sync)
    self._character_device.seek(pos)