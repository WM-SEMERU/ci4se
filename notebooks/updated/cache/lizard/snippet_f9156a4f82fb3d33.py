def template_cylinder_annulus(height, outer_radius, inner_radius=0):
    r
    img = _template_sphere_disc(dim=2, outer_radius=outer_radius,
        inner_radius=inner_radius)
    img = sp.tile(sp.atleast_3d(img), reps=height)
    return img