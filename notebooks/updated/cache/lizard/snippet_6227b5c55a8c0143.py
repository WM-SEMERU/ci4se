def get_kpoint_degeneracy(self, kpoint, cartesian=False, tol=0.01):
    all_kpts = self.get_sym_eq_kpoints(kpoint, cartesian, tol=tol)
    if all_kpts is not None:
        return len(all_kpts)