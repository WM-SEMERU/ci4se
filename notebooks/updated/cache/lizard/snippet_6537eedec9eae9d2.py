def read_lamination_parameters(thickness, laminaprop, rho, xiA1, xiA2, xiA3,
    xiA4, xiB1, xiB2, xiB3, xiB4, xiD1, xiD2, xiD3, xiD4, xiE1, xiE2, xiE3,
    xiE4):
    r
    lam = Laminate()
    lam.h = thickness
    lam.matobj = read_laminaprop(laminaprop, rho)
    lam.xiA = np.array([1, xiA1, xiA2, xiA3, xiA4], dtype=np.float64)
    lam.xiB = np.array([0, xiB1, xiB2, xiB3, xiB4], dtype=np.float64)
    lam.xiD = np.array([1, xiD1, xiD2, xiD3, xiD4], dtype=np.float64)
    lam.xiE = np.array([1, xiE1, xiE2, xiE3, xiE4], dtype=np.float64)
    lam.calc_ABDE_from_lamination_parameters()
    return lam