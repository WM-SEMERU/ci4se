def is_perfect_consonant(note1, note2, include_fourths=True):
    dhalf = measure(note1, note2)
    return dhalf in [0, 7] or include_fourths and dhalf == 5