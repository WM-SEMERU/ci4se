def get_inertia_tensor(elements, coordinates):
    pow2 = coordinates ** 2
    molecular_weight = np.array([[atomic_mass[e.upper()]] for e in elements])
    diag_1 = np.sum(molecular_weight * (pow2[:, (1)] + pow2[:, (2)]))
    diag_2 = np.sum(molecular_weight * (pow2[:, (0)] + pow2[:, (2)]))
    diag_3 = np.sum(molecular_weight * (pow2[:, (0)] + pow2[:, (1)]))
    mxy = np.sum(-molecular_weight * coordinates[:, (0)] * coordinates[:, (1)])
    mxz = np.sum(-molecular_weight * coordinates[:, (0)] * coordinates[:, (2)])
    myz = np.sum(-molecular_weight * coordinates[:, (1)] * coordinates[:, (2)])
    inertia_tensor = np.array([[diag_1, mxy, mxz], [mxy, diag_2, myz], [mxz,
        myz, diag_3]]) / coordinates.shape[0]
    return inertia_tensor