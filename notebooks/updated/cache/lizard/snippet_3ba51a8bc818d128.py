def find_pix_borders(sp, sought_value):
    if sp.ndim != 1:
        raise ValueError('Unexpected number of dimensions:', sp.ndim)
    naxis1 = len(sp)
    jborder_min = -1
    jborder_max = naxis1
    if not np.alltrue(sp == sought_value):
        while True:
            jborder_min += 1
            if sp[jborder_min] != sought_value:
                break
        while True:
            jborder_max -= 1
            if sp[jborder_max] != sought_value:
                break
    return jborder_min, jborder_max