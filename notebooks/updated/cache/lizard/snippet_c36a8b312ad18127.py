def lbd_to_XYZ(l, b, d, degree=False):
    return nu.array([d * nu.cos(b) * nu.cos(l), d * nu.cos(b) * nu.sin(l), 
        d * nu.sin(b)]).T