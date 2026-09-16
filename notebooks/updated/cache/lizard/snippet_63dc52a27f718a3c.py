def potential_vorticity_barotropic(heights, u, v, dx, dy, lats, dim_order='yx'
    ):
    r
    avor = absolute_vorticity(u, v, dx, dy, lats, dim_order=dim_order)
    return (avor / heights).to('meter**-1 * second**-1')