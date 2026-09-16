def by_population_density(self, lower=-1, upper=2 ** 31, zipcode_type=
    ZipcodeType.Standard, sort_by=SimpleZipcode.population_density.name,
    ascending=False, returns=DEFAULT_LIMIT):
    return self.query(population_density_lower=lower,
        population_density_upper=upper, sort_by=sort_by, zipcode_type=
        zipcode_type, ascending=ascending, returns=returns)