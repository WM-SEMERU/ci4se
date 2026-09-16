def gen_reference_primitive(polypeptide, start, end):
    prim = polypeptide.primitive
    q = find_foot(a=start, b=end, p=prim.coordinates[0])
    ax = Axis(start=q, end=end)
    if not is_acute(polypeptide_vector(polypeptide), ax.unit_tangent):
        ax = Axis(start=end, end=q)
    arc_length = 0
    points = [ax.start]
    for rise in prim.rise_per_residue()[:-1]:
        arc_length += rise
        t = ax.t_from_arc_length(arc_length=arc_length)
        point = ax.point(t)
        points.append(point)
    reference_primitive = Primitive.from_coordinates(points)
    return reference_primitive