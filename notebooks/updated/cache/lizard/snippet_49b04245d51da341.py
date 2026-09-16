def characters(self):
    chars = 0
    for fragment in self.fragments:
        chars += fragment.characters
    return chars