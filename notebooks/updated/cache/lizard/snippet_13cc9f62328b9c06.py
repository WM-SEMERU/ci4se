def basis_states(self):
    from qnet.algebra.core.state_algebra import BasisKet, TensorKet
    ls_bases = [ls.basis_labels for ls in self.local_factors]
    for label_tuple in cartesian_product(*ls_bases):
        yield TensorKet(*[BasisKet(label, hs=ls) for ls, label in zip(self.
            local_factors, label_tuple)])