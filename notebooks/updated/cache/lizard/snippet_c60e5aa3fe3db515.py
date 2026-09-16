def predict(x, P, F=1, Q=0, u=0, B=1, alpha=1.0):
    if np.isscalar(F):
        F = np.array(F)
    x = dot(F, x) + dot(B, u)
    P = alpha * alpha * dot(dot(F, P), F.T) + Q
    return x, P