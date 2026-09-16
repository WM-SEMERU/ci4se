def draw_default(self, inside=5, outside=15):
    if 'outer_space' in self.config.solar_class_index:
        self.selection_array[:, :] = self.config.solar_class_index[
            'outer_space']
    elif 'empty_outer_space' in self.config.solar_class_index:
        self.selection_array[:, :] = self.config.solar_class_index[
            'empty_outer_space']
    else:
        raise ValueError(
            'outer_space or empty_outer_space must be classes with colors.')
    self.draw_annulus((self.cx, self.cy), self.sun_radius_pixel - inside, 
        self.sun_radius_pixel + outside, self.selection_array, self.config.
        solar_class_index['limb'])
    self.draw_circle((self.cx, self.cy), self.sun_radius_pixel - inside,
        self.selection_array, self.config.solar_class_index['quiet_sun'])