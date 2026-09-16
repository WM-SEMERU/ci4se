def get_ra(self):
    try:
        return self.ra.value
    except AttributeError:
        return self.sky_coord.transform_to('icrs').ra.value