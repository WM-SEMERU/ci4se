def calc_efficiency(self):
    cell_power = self.calc_power_density()
    solar_power = self.calc_blackbody_radiant_power_density()
    efficiency = cell_power / solar_power
    return efficiency.decompose().value