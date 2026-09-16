def read_laminaprop(laminaprop=None, rho=None):
    matlam = MatLamina()
    if laminaprop == None:
        error('laminaprop must be a tuple in the following format:\n\t' +
            '(e1, e2, nu12, g12, g13, g23, e3, nu13, nu23)')
    if len(laminaprop) == 3:
        e = laminaprop[0]
        nu = laminaprop[2]
        g = e / (2 * (1 + nu))
        laminaprop = e, e, nu, g, g, g, e, nu, nu
    nu12 = laminaprop[2]
    if len(laminaprop) < 9:
        e2 = laminaprop[1]
        laminaprop = tuple(list(laminaprop)[:6] + [e2, nu12, nu12])
    matlam.e1 = laminaprop[0]
    matlam.e2 = laminaprop[1]
    matlam.e3 = laminaprop[6]
    matlam.nu12 = laminaprop[2]
    matlam.nu13 = laminaprop[7]
    matlam.nu23 = laminaprop[8]
    matlam.nu21 = matlam.nu12 * matlam.e2 / matlam.e1
    matlam.nu31 = matlam.nu13 * matlam.e3 / matlam.e1
    matlam.nu32 = matlam.nu23 * matlam.e3 / matlam.e2
    matlam.g12 = laminaprop[3]
    matlam.g13 = laminaprop[4]
    matlam.g23 = laminaprop[5]
    matlam.rho = rho
    matlam.rebuild()
    return matlam