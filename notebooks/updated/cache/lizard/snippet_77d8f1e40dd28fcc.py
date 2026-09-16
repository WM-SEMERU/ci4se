def chi_p_from_spherical(mass1, mass2, spin1_a, spin1_azimuthal,
    spin1_polar, spin2_a, spin2_azimuthal, spin2_polar):
    spin1x, spin1y, _ = _spherical_to_cartesian(spin1_a, spin1_azimuthal,
        spin1_polar)
    spin2x, spin2y, _ = _spherical_to_cartesian(spin2_a, spin2_azimuthal,
        spin2_polar)
    return chi_p(mass1, mass2, spin1x, spin1y, spin2x, spin2y)