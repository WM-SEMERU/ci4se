def from_dict(cls, d):
    sites = [Site.from_dict(sd) for sd in d['sites']]
    charge = d.get('charge', 0)
    spin_multiplicity = d.get('spin_multiplicity')
    return cls.from_sites(sites, charge=charge, spin_multiplicity=
        spin_multiplicity)