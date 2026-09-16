def ellipse(center, covariance_matrix, level=1, n=1000):
    U, s, rotation_matrix = N.linalg.svd(covariance_matrix)
    saxes = N.sqrt(s) * level
    u = N.linspace(0, 2 * N.pi, n)
    data = N.column_stack((saxes[0] * N.cos(u), saxes[1] * N.sin(u)))
    return N.dot(data, rotation_matrix) + center