def voice_channels(self):
    r = [ch for ch in self._channels.values() if isinstance(ch, VoiceChannel)]
    r.sort(key=lambda c: (c.position, c.id))
    return r