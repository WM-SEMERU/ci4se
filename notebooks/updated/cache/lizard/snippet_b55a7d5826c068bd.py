def set_charge_and_spin(self, charge, spin_multiplicity=None):
    self._charge = charge
    nelectrons = 0
    for site in self._sites:
        for sp, amt in site.species.items():
            if not isinstance(sp, DummySpecie):
                nelectrons += sp.Z * amt
    nelectrons -= charge
    self._nelectrons = nelectrons
    if spin_multiplicity:
        if (nelectrons + spin_multiplicity) % 2 != 1:
            raise ValueError(
                'Charge of {} and spin multiplicity of {} is not possible for this molecule'
                .format(self._charge, spin_multiplicity))
        self._spin_multiplicity = spin_multiplicity
    else:
        self._spin_multiplicity = 1 if nelectrons % 2 == 0 else 2