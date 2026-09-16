def trim_trailing_silence(self):
    active_length = self.get_active_length()
    for track in self.tracks:
        track.pianoroll = track.pianoroll[:active_length]