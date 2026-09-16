def clean(self):
    self.suggest = {'input': [' '.join(p) for p in permutations(self.name.
        split())], 'weight': self.popularity}