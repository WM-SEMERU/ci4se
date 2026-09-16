def get_plan_from_dual(alpha, beta, C, regul):
    X = alpha[:, (np.newaxis)] + beta - C
    return regul.delta_Omega(X)[1]