def step1c(self):
    if self.ends(['y']) and self.vowel_in_stem():
        self.b[self.k] = 'i'