def decompose(self):
    mc = self._get_subclass('MoleculeContainer')
    reactants = mc()
    products = mc()
    for n, atom in self.atoms():
        reactants.add_atom(atom._reactant, n)
        products.add_atom(atom._product, n)
    for n, m, bond in self.bonds():
        if bond._reactant is not None:
            reactants.add_bond(n, m, bond._reactant)
        if bond._product is not None:
            products.add_bond(n, m, bond._product)
    return reactants, products