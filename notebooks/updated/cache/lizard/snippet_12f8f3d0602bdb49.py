def within_joyner_boore_distance(self, surface, distance, **kwargs):
    upper_depth, lower_depth = _check_depth_limits(kwargs)
    rjb = surface.get_joyner_boore_distance(self.catalogue.
        hypocentres_as_mesh())
    is_valid = np.logical_and(rjb <= distance, np.logical_and(self.
        catalogue.data['depth'] >= upper_depth, self.catalogue.data['depth'
        ] < lower_depth))
    return self.select_catalogue(is_valid)