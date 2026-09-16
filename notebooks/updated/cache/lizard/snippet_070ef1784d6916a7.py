def _compute_syllable(self, text):
    is_in_onset = True
    is_in_nucleus = False
    is_in_coda = False
    if len(text) > 0:
        for c in text:
            if is_in_onset and c in self.consonants:
                self.onset.append(c)
            elif is_in_onset and c in self.vowels:
                is_in_onset = False
                is_in_nucleus = True
                self.nucleus.append(c)
            elif is_in_nucleus and c in self.vowels:
                self.nucleus.append(c)
            elif is_in_nucleus and c in self.consonants:
                is_in_nucleus = False
                is_in_coda = True
                self.coda.append(c)
            elif is_in_coda and c in self.consonants:
                self.coda.append(c)
            elif is_in_coda and c in self.vowels:
                raise ValueError(
                    "This is not a correct syllable (a vowel '{}' cannot be inserted in coda)"
                    .format(c))
            else:
                raise ValueError('{} is an unknown character'.format(c))
        if len(self.nucleus) == 0:
            raise ValueError('This is not a correct syllable')
    else:
        raise ValueError("A syllable can't be void")