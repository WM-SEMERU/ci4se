def from_mass_fractions(cls, mass_fractions, formula=None):
    mass_fractions = process_wildcard(mass_fractions)
    atomic_fractions = convert_mass_to_atomic_fractions(mass_fractions)
    if not formula:
        formula = generate_name(atomic_fractions)
    return cls(cls._key, mass_fractions, atomic_fractions, formula)