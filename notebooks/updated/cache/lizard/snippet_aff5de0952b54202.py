def planar_matrix_to_3D(matrix_2D):
    matrix_2D = np.asanyarray(matrix_2D, dtype=np.float64)
    if matrix_2D.shape != (3, 3):
        raise ValueError('Homogenous 2D transformation matrix required!')
    matrix_3D = np.eye(4)
    matrix_3D[0:2, (3)] = matrix_2D[0:2, (2)]
    matrix_3D[0:2, 0:2] = matrix_2D[0:2, 0:2]
    return matrix_3D