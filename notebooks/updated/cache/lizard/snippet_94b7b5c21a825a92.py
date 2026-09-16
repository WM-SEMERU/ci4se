def gen_sl_transform_matricies(area_multiple):
    return [np.array(((i, j), (0, area_multiple / i))) for i in get_factors
        (area_multiple) for j in range(area_multiple // i)]