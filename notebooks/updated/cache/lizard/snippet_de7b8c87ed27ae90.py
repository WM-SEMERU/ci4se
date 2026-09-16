def outlier_cutoff(a, threshold=3.5):
    A = np.array(a, dtype=float)
    M = np.median(A)
    D = np.absolute(A - M)
    MAD = np.median(D)
    C = threshold / 0.67449 * MAD
    return M - C, M + C