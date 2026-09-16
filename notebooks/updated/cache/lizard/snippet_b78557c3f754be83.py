def sample(self, count, **kwargs):
    poly = self.polygons_full
    if len(poly) == 0:
        samples = np.array([])
    elif len(poly) == 1:
        samples = polygons.sample(poly[0], count=count, **kwargs)
    else:
        samples = util.vstack_empty([polygons.sample(i, count=count, **
            kwargs) for i in poly])
    return samples