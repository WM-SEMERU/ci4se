def windings_aligned(triangles, normals_compare):
    triangles = np.asanyarray(triangles, dtype=np.float64)
    if not util.is_shape(triangles, (-1, 3, 3)):
        raise ValueError('Triangles must be (n,3,3)!')
    calculated, valid = normals(triangles)
    difference = util.diagonal_dot(calculated, normals_compare[valid])
    aligned = np.zeros(len(triangles), dtype=np.bool)
    aligned[valid] = difference > 0.0
    return aligned