def transform(mesh, translation_scale=1000.0):
    matrix = transformations.random_rotation_matrix()
    matrix[0:3, (3)] = np.random.random(3) * translation_scale
    triangles = np.random.permutation(mesh.triangles).reshape((-1, 3))
    triangles = transformations.transform_points(triangles, matrix)
    mesh_type = util.type_named(mesh, 'Trimesh')
    permutated = mesh_type(**triangles_module.to_kwargs(triangles.reshape((
        -1, 3, 3))))
    return permutated