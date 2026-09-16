def Luv_to_XYZ(cobj, *args, **kwargs):
    illum = cobj.get_illuminant_xyz()
    if cobj.luv_l <= 0.0:
        xyz_x = 0.0
        xyz_y = 0.0
        xyz_z = 0.0
        return XYZColor(xyz_x, xyz_y, xyz_z, observer=cobj.observer,
            illuminant=cobj.illuminant)
    cie_k_times_e = color_constants.CIE_K * color_constants.CIE_E
    u_sub_0 = 4.0 * illum['X'] / (illum['X'] + 15.0 * illum['Y'] + 3.0 *
        illum['Z'])
    v_sub_0 = 9.0 * illum['Y'] / (illum['X'] + 15.0 * illum['Y'] + 3.0 *
        illum['Z'])
    var_u = cobj.luv_u / (13.0 * cobj.luv_l) + u_sub_0
    var_v = cobj.luv_v / (13.0 * cobj.luv_l) + v_sub_0
    if cobj.luv_l > cie_k_times_e:
        xyz_y = math.pow((cobj.luv_l + 16.0) / 116.0, 3.0)
    else:
        xyz_y = cobj.luv_l / color_constants.CIE_K
    xyz_x = xyz_y * 9.0 * var_u / (4.0 * var_v)
    xyz_z = xyz_y * (12.0 - 3.0 * var_u - 20.0 * var_v) / (4.0 * var_v)
    return XYZColor(xyz_x, xyz_y, xyz_z, illuminant=cobj.illuminant,
        observer=cobj.observer)