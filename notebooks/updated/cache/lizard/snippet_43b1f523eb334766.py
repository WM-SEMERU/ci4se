def semi_dual_obj_grad(alpha, a, b, C, regul):
    obj = np.dot(alpha, a)
    grad = a.copy()
    X = alpha[:, (np.newaxis)] - C
    val, G = regul.max_Omega(X, b)
    obj -= np.dot(b, val)
    grad -= np.dot(G, b)
    return obj, grad