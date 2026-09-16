def replace_coord(self, i):
    da = next(islice(self.data_iterator, i, i + 1))
    name, coord = self.get_alternative_coord(da, i)
    other_coords = {key: da.coords[key] for key in set(da.coords).
        difference(da.dims)}
    ret = da.rename({da.dims[-1]: name}).assign_coords(**{name: coord}
        ).assign_coords(**other_coords)
    return ret