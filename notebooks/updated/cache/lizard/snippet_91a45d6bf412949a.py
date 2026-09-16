def get_inert_ratio_raw(cont):
    if isinstance(cont, np.ndarray):
        cont = [cont]
        ret_list = False
    else:
        ret_list = True
    length = len(cont)
    inert_ratio_raw = np.zeros(length, dtype=float) * np.nan
    for ii in range(length):
        moments = cont_moments_cv(cont[ii])
        if moments is not None:
            inert_ratio_raw[ii] = np.sqrt(moments['mu20'] / moments['mu02'])
    if not ret_list:
        inert_ratio_raw = inert_ratio_raw[0]
    return inert_ratio_raw