def play_note(self, note, duration, volume=100, play_type=
    PLAY_WAIT_FOR_COMPLETE):
    self._validate_play_type(play_type)
    try:
        freq = self._NOTE_FREQUENCIES.get(note.upper(), self.
            _NOTE_FREQUENCIES[note])
    except KeyError:
        raise ValueError('invalid note (%s)' % note)
    if duration <= 0:
        raise ValueError('invalid duration (%s)' % duration)
    if not 0 < volume <= 100:
        raise ValueError('invalid volume (%s)' % volume)
    return self.play_tone(freq, duration=duration, volume=volume, play_type
        =play_type)