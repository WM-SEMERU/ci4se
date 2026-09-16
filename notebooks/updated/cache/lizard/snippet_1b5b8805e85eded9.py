def transform(self, maps):
    out = {parameters.redshift: cosmology.redshift(maps[parameters.distance])}
    return self.format_output(maps, out)