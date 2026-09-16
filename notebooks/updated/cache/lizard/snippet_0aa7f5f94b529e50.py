def ts(self, data, lon_cyclic=True, lon_str=LON_STR, lat_str=LAT_STR,
    land_mask_str=LAND_MASK_STR, sfc_area_str=SFC_AREA_STR):
    data_masked = self.mask_var(data, lon_cyclic=lon_cyclic, lon_str=
        lon_str, lat_str=lat_str)
    sfc_area = data[sfc_area_str]
    sfc_area_masked = self.mask_var(sfc_area, lon_cyclic=lon_cyclic,
        lon_str=lon_str, lat_str=lat_str)
    land_mask = _get_land_mask(data, self.do_land_mask, land_mask_str=
        land_mask_str)
    weights = sfc_area_masked * land_mask
    weights = weights.where(np.isfinite(data))
    weights_reg_sum = weights.sum(lon_str).sum(lat_str)
    data_reg_sum = (data_masked * sfc_area_masked * land_mask).sum(lat_str
        ).sum(lon_str)
    return data_reg_sum / weights_reg_sum