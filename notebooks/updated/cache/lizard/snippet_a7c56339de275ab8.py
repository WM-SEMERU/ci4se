def __ticker_midi_note(x, pos):
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    cents = float(np.mod(x, 1.0))
    if cents >= 0.5:
        cents = cents - 1.0
        x = x + 0.5
    idx = int(x % 12)
    octave = int(x / 12) - 1
    if cents == 0:
        return '{:s}{:2d}'.format(NOTES[idx], octave)
    return '{:s}{:2d}{:+02d}'.format(NOTES[idx], octave, int(cents * 100))