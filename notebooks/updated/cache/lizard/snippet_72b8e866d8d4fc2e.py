def spherical_matrix(theta, phi, axes='sxyz'):
    result = euler_matrix(0.0, phi, theta, axes=axes)
    return result