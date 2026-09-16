def get_structures(self, chemsys_formula_id, final=True):
    prop = 'final_structure' if final else 'initial_structure'
    data = self.get_data(chemsys_formula_id, prop=prop)
    return [d[prop] for d in data]