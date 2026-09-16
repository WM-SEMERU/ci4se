def sph_midpoint(coord1, coord2):
    c1 = coord1.cartesian / coord1.cartesian.norm()
    coord2 = coord2.transform_to(coord1.frame)
    c2 = coord2.cartesian / coord2.cartesian.norm()
    midpt = 0.5 * (c1 + c2)
    usph = midpt.represent_as(coord.UnitSphericalRepresentation)
    return coord1.frame.realize_frame(usph)