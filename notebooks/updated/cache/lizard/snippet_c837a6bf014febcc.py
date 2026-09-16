def mother(self):
    if self._mother == []:
        self._mother = self.sub_tag('FAMC/WIFE')
    return self._mother