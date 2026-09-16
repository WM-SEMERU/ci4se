def _get_reference_band(self, data):
    nir = data[..., self.nir_idx].astype('float32')
    red = data[..., self.red_idx].astype('float32')
    return (nir - red) / (nir + red)