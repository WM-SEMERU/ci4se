def get_slabs(self, bonds=None, ftol=0.1, tol=0.1, max_broken_bonds=0,
    symmetrize=False, repair=False):
    c_ranges = set() if bonds is None else self._get_c_ranges(bonds)
    slabs = []
    for shift in self._calculate_possible_shifts(tol=ftol):
        bonds_broken = 0
        for r in c_ranges:
            if r[0] <= shift <= r[1]:
                bonds_broken += 1
        slab = self.get_slab(shift, tol=tol, energy=bonds_broken)
        if bonds_broken <= max_broken_bonds:
            slabs.append(slab)
        elif repair:
            slabs.append(self.repair_broken_bonds(slab, bonds))
    m = StructureMatcher(ltol=tol, stol=tol, primitive_cell=False, scale=False)
    new_slabs = []
    for g in m.group_structures(slabs):
        if symmetrize:
            slabs = self.nonstoichiometric_symmetrized_slab(g[0])
            new_slabs.extend(slabs)
        else:
            new_slabs.append(g[0])
    match = StructureMatcher(ltol=tol, stol=tol, primitive_cell=False,
        scale=False)
    new_slabs = [g[0] for g in match.group_structures(new_slabs)]
    return sorted(new_slabs, key=lambda s: s.energy)