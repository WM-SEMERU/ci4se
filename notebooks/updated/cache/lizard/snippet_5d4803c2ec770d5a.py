def get_lps(self):
    if self.header is not None:
        for linguisticProcessor in self.header:
            for lp in linguisticProcessor:
                yield lp