def _get_reaction(self, x):
    mix_comp = self.comp1 * x + self.comp2 * (1 - x)
    decomp = self.pd.get_decomposition(mix_comp)
    if np.isclose(x, 0):
        reactant = [self.c2_original]
    elif np.isclose(x, 1):
        reactant = [self.c1_original]
    else:
        reactant = list(set([self.c1_original, self.c2_original]))
    if self.grand:
        reactant += [Composition(e.symbol) for e, v in self.pd.chempots.items()
            ]
    product = [Composition(k.name) for k, v in decomp.items()]
    reaction = Reaction(reactant, product)
    x_original = self._get_original_composition_ratio(reaction)
    if np.isclose(x_original, 1):
        reaction.normalize_to(self.c1_original, x_original)
    else:
        reaction.normalize_to(self.c2_original, 1 - x_original)
    return reaction