def remove_observations_below_value(x, y, z, val=0):
    r
    x_ = x[z >= val]
    y_ = y[z >= val]
    z_ = z[z >= val]
    return x_, y_, z_