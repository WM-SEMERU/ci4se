def apply_grad_cartesian_tensor(grad_X, zmat_dist):
    columns = ['bond', 'angle', 'dihedral']
    C_dist = zmat_dist.loc[:, (columns)].values.T
    try:
        C_dist = C_dist.astype('f8')
        C_dist[([1, 2]), :] = np.radians(C_dist[([1, 2]), :])
    except (TypeError, AttributeError):
        C_dist[([1, 2]), :] = sympy.rad(C_dist[([1, 2]), :])
    cart_dist = np.tensordot(grad_X, C_dist, axes=([3, 2], [0, 1])).T
    from chemcoord.cartesian_coordinates.cartesian_class_main import Cartesian
    return Cartesian(atoms=zmat_dist['atom'], coords=cart_dist, index=
        zmat_dist.index)