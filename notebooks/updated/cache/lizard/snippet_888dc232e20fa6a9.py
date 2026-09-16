def discretize_soil_profile(sp, incs=None, target=1.0):
    if incs is None:
        incs = np.ones(sp.n_layers) * target
    dd = {}
    dd['thickness'] = []
    dd['unit_mass'] = []
    dd['shear_vel'] = []
    cum_thickness = 0
    for i in range(sp.n_layers):
        sl = sp.layer(i + 1)
        thickness = sp.layer_height(i + 1)
        n_slices = max(int(thickness / incs[i]), 1)
        slice_thickness = float(thickness) / n_slices
        for j in range(n_slices):
            cum_thickness += slice_thickness
            if cum_thickness >= sp.gwl:
                rho = sl.unit_sat_mass
                saturation = True
            else:
                rho = sl.unit_dry_mass
                saturation = False
            if hasattr(sl, 'get_shear_vel_at_v_eff_stress'):
                v_eff = sp.vertical_effective_stress(cum_thickness)
                vs = sl.get_shear_vel_at_v_eff_stress(v_eff, saturation)
            else:
                vs = sl.calc_shear_vel(saturation)
            dd['shear_vel'].append(vs)
            dd['unit_mass'].append(rho)
            dd['thickness'].append(slice_thickness)
    for item in dd:
        dd[item] = np.array(dd[item])
    return dd