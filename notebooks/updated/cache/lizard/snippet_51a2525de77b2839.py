def model_counts_map(self, name=None, exclude=None, use_mask=False):
    maps = [c.model_counts_map(name, exclude, use_mask=use_mask) for c in
        self.components]
    return skymap.coadd_maps(self.geom, maps)