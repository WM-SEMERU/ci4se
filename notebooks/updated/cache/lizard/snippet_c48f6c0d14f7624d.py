def setup_keys(self):
    discovery_methods = {}
    discovery_years = {}
    nan_list = []
    for planet in self.planet_list:
        if 'Solar System' in planet.params['list'
            ] and self.skip_solar_system_planets:
            continue
        try:
            discovery_methods[planet.discoveryMethod] += 1
        except KeyError:
            discovery_methods[planet.discoveryMethod] = 1
        try:
            discovery_years[planet.discoveryYear] += 1
        except KeyError:
            discovery_years[planet.discoveryYear] = 1
        if planet.discoveryMethod is np.nan:
            nan_list.append(planet)
    self.nan_list = nan_list
    return discovery_years