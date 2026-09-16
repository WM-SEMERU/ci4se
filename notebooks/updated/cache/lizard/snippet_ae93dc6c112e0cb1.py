def _apply_aeff_corrections(intensity_map, aeff_corrections):
    data = aeff_corrections * intensity_map.data.T
    return HpxMap(data.T, intensity_map.hpx)