def filter_humphrey(mesh, alpha=0.1, beta=0.5, iterations=10,
    laplacian_operator=None):
    if laplacian_operator is None:
        laplacian_operator = laplacian_calculation(mesh)
    vertices = mesh.vertices.copy().view(np.ndarray)
    original = vertices.copy()
    for _index in range(iterations):
        vert_q = vertices.copy()
        vertices = laplacian_operator.dot(vertices)
        vert_b = vertices - (alpha * original + (1.0 - alpha) * vert_q)
        vertices -= beta * vert_b + (1.0 - beta) * laplacian_operator.dot(
            vert_b)
    mesh.vertices = vertices
    return mesh