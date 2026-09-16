def from_interval_shorthand(self, startnote, shorthand, up=True):
    self.empty()
    if type(startnote) == str:
        startnote = Note(startnote)
    n = Note(startnote.name, startnote.octave, startnote.dynamics)
    n.transpose(shorthand, up)
    self.add_notes([startnote, n])
    return self