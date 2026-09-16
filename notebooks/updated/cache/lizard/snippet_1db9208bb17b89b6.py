def vector_projection(v1, v2):
    return scalar_projection(v1, v2) * v2 / np.linalg.norm(v2)