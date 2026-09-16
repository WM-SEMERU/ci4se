def symmetrize(self, max_n=10, tolerance=0.3, epsilon=0.001):
    mg_mol = self.get_pymatgen_molecule()
    eq = iterative_symmetrize(mg_mol, max_n=max_n, tolerance=tolerance,
        epsilon=epsilon)
    self._convert_eq(eq)
    return eq