def admeig(classname, f, m_u, m_d, m_s, m_c, m_b, m_e, m_mu, m_tau):
    args = f, m_u, m_d, m_s, m_c, m_b, m_e, m_mu, m_tau
    A = getattr(adm, 'adm_s_' + classname)(*args)
    perm_keys = get_permissible_wcs(classname, f)
    if perm_keys != 'all':
        A = A[perm_keys][:, (perm_keys)]
    w, v = np.linalg.eig(A.T)
    return w, v