def set_default_region(self, region):
    region = _convert_to_charp(region)
    self._set_default_region_func(self.alpr_pointer, region)