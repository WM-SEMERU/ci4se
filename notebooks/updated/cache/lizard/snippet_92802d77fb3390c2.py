def generate_notes(notes):
    new_notes = []
    for note in notes:
        tmp_note = {}
        for note_item in notes[note]:
            tmp_note[note_item] = notes[note][note_item]
        new_notes.append(tmp_note)
    return new_notes