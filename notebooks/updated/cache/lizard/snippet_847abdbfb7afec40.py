def laplacian_calculation(mesh, equal_weight=True):
    neighbors = mesh.vertex_neighbors
    vertices = mesh.vertices.view(np.ndarray)
    col = np.concatenate(neighbors)
    row = np.concatenate([([i] * len(n)) for i, n in enumerate(neighbors)])
    if equal_weight:
        data = np.concatenate([([1.0 / len(n)] * len(n)) for n in neighbors])
    else:
        ones = np.ones(3)
        norms = [(1.0 / np.sqrt(np.dot((vertices[i] - vertices[n]) ** 2,
            ones))) for i, n in enumerate(neighbors)]
        data = np.concatenate([(i / i.sum()) for i in norms])
    matrix = coo_matrix((data, (row, col)), shape=[len(vertices)] * 2)
    return matrix