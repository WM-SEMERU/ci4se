def getUe(classname, eta_s, f, alpha_s, alpha_e, m_u, m_d, m_s, m_c, m_b,
    m_e, m_mu, m_tau):
    args = f, m_u, m_d, m_s, m_c, m_b, m_e, m_mu, m_tau
    A = getattr(adm, 'adm_e_' + classname)(*args)
    perm_keys = get_permissible_wcs(classname, f)
    if perm_keys != 'all':
        A = A[perm_keys][:, (perm_keys)]
    w, v = admeig(classname, *args)
    b0s = 11 - 2 * f / 3
    a = w / (2 * b0s)
    K = np.linalg.inv(v) @ A.T @ v
    for i in range(K.shape[0]):
        for j in range(K.shape[1]):
            if a[i] - a[j] != 1:
                K[i, j] *= (eta_s ** (a[j] + 1) - eta_s ** a[i]) / (a[i] -
                    a[j] - 1)
            else:
                K[i, j] *= eta_s ** a[i] * log(1 / eta_s)
    return -alpha_e / (2 * b0s * alpha_s) * v @ K @ np.linalg.inv(v)