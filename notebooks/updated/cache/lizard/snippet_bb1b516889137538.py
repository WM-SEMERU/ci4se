def stop_Note(self, note, channel=1):
    if hasattr(note, 'channel'):
        channel = note.channel
    self.stop_event(int(note) + 12, int(channel))
    self.notify_listeners(self.MSG_STOP_INT, {'channel': int(channel),
        'note': int(note) + 12})
    self.notify_listeners(self.MSG_STOP_NOTE, {'channel': int(channel),
        'note': note})
    return True