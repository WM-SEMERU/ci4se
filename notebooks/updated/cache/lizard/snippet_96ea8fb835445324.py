def rouwenhorst(rho, sigma, N):
    from numpy import sqrt, linspace, array, zeros
    sigma = float(sigma)
    if N == 1:
        nodes = array([0.0])
        transitions = array([[1.0]])
        return [nodes, transitions]
    p = (rho + 1) / 2
    q = p
    nu = sqrt((N - 1) / (1 - rho ** 2)) * sigma
    nodes = linspace(-nu, nu, N)
    sig_a = sigma
    n = 1
    mat0 = array([[p, 1 - p], [1 - q, q]])
    if N == 2:
        return [nodes, mat0]
    for n in range(3, N + 1):
        mat = zeros((n, n))
        mat_A = mat.copy()
        mat_B = mat.copy()
        mat_C = mat.copy()
        mat_D = mat.copy()
        mat_A[:-1, :-1] = mat0
        mat_B[:-1, 1:] = mat0
        mat_C[1:, :-1] = mat0
        mat_D[1:, 1:] = mat0
        mat0 = p * mat_A + (1 - p) * mat_B + (1 - q) * mat_C + q * mat_D
        mat0[1:-1, :] = mat0[1:-1, :] / 2
    P = mat0
    return [nodes, P]