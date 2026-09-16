def load_midi_file(path):
    midi_notes = []

    def register_note(track, channel, pitch, velocity, start, end):
        midi_notes.append((pitch, start, end))
    midi.register_note = register_note
    global m
    m = midi.MidiFile()
    m.open(midi_path)
    m.read()
    m.close()
    for pitch, start, end in midi_notes:
        start /= m.ticksPerQuarterNote
        end /= m.ticksPerQuarterNote
        yield pitch, start, end