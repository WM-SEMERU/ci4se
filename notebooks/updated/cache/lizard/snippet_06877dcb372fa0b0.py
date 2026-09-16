def Dir_anis_corr(InDir, AniSpec):
    Dir = np.zeros(3, 'f')
    Dir[0] = InDir[0]
    Dir[1] = InDir[1]
    Dir[2] = 1.0
    chi, chi_inv = check_F(AniSpec)
    if chi[0][0] == 1.0:
        return Dir
    X = dir2cart(Dir)
    M = np.array(X)
    H = np.dot(M, chi_inv)
    return cart2dir(H)