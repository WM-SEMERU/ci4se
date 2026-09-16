def get_composition(self):
    strc = self.get_output_structure()
    counts = Counter(strc.get_chemical_symbols())
    return ''.join(k if counts[k] == 1 else '%s%d' % (k, counts[k]) for k in
        sorted(counts))