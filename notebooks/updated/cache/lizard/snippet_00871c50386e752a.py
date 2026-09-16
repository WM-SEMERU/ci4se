def transform(self, maps):
    mass1 = maps[parameters.mass1]
    mass2 = maps[parameters.mass2]
    out = {}
    out[parameters.spin1z] = conversions.spin1z_from_mass1_mass2_chi_eff_chi_a(
        mass1, mass2, maps[parameters.chi_eff], maps['chi_a'])
    out[parameters.spin2z] = conversions.spin2z_from_mass1_mass2_chi_eff_chi_a(
        mass1, mass2, maps[parameters.chi_eff], maps['chi_a'])
    return self.format_output(maps, out)