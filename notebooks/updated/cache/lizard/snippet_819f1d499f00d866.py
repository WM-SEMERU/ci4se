def merge_odd_even_csu_configurations(conf_odd, conf_even):
    merged_conf = deepcopy(conf_odd)
    for i in range(EMIR_NBARS):
        ibar = i + 1
        if ibar % 2 == 0:
            merged_conf._csu_bar_left[i] = conf_even._csu_bar_left[i]
            merged_conf._csu_bar_right[i] = conf_even._csu_bar_right[i]
            merged_conf._csu_bar_slit_center[i
                ] = conf_even._csu_bar_slit_center[i]
            merged_conf._csu_bar_slit_width[i] = conf_even._csu_bar_slit_width[
                i]
    return merged_conf