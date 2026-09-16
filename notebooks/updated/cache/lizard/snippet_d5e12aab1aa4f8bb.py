def CMY_to_CMYK(cobj, *args, **kwargs):
    var_k = 1.0
    if cobj.cmy_c < var_k:
        var_k = cobj.cmy_c
    if cobj.cmy_m < var_k:
        var_k = cobj.cmy_m
    if cobj.cmy_y < var_k:
        var_k = cobj.cmy_y
    if var_k == 1:
        cmyk_c = 0.0
        cmyk_m = 0.0
        cmyk_y = 0.0
    else:
        cmyk_c = (cobj.cmy_c - var_k) / (1.0 - var_k)
        cmyk_m = (cobj.cmy_m - var_k) / (1.0 - var_k)
        cmyk_y = (cobj.cmy_y - var_k) / (1.0 - var_k)
    cmyk_k = var_k
    return CMYKColor(cmyk_c, cmyk_m, cmyk_y, cmyk_k)