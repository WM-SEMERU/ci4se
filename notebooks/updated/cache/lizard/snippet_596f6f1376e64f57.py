def layer_mapping(self, mapping):
    if self.inherit_aes:
        aesthetics = defaults(self.mapping, mapping)
    else:
        aesthetics = self.mapping
    calculated = set(get_calculated_aes(aesthetics))
    d = dict((ae, v) for ae, v in aesthetics.items() if ae not in self.geom
        .aes_params and ae not in calculated)
    self._active_mapping = aes(**d)
    return self._active_mapping