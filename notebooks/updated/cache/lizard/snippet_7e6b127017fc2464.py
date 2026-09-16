def compute_zoom_level(bounds, domain, levels):
    area_fraction = min(bounds.area / domain.area, 1)
    return int(min(round(np.log2(1 / area_fraction)), levels))