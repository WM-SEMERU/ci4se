def symbolic_rotation_matrix(phi, theta, symbolic_psi):
    return sympy.Matrix(Rz_matrix(phi)) * sympy.Matrix(Rx_matrix(theta)
        ) * symbolic_Rz_matrix(symbolic_psi)