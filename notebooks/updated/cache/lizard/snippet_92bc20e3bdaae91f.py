def get_direct_band_gap(self):
    if self.is_metal():
        return 0.0
    dg = self.get_direct_band_gap_dict()
    return min(v['value'] for v in dg.values())