def m_s(ms2, scale, f, alphasMZ=0.1185, loop=3):
    r
    if scale == 2 and f == 3:
        return ms2
    _sane(scale, f)
    crd = rundec.CRunDec()
    alphas_2 = alpha_s(2, 3, alphasMZ=alphasMZ, loop=loop)
    if f == 3:
        alphas_scale = alpha_s(scale, f, alphasMZ=alphasMZ, loop=loop)
        return crd.mMS2mMS(ms2, alphas_2, alphas_scale, f, loop)
    elif f == 4:
        crd.nfMmu.Mth = 1.3
        crd.nfMmu.muth = 1.3
        crd.nfMmu.nf = 4
        return crd.mL2mH(ms2, alphas_2, 2, crd.nfMmu, scale, loop)
    elif f == 5:
        mc = 1.3
        crd.nfMmu.Mth = mc
        crd.nfMmu.muth = mc
        crd.nfMmu.nf = 4
        msmc = crd.mL2mH(ms2, alphas_2, 2, crd.nfMmu, mc, loop)
        crd.nfMmu.Mth = 4.8
        crd.nfMmu.muth = 4.8
        crd.nfMmu.nf = 5
        alphas_mc = alpha_s(mc, 4, alphasMZ=alphasMZ, loop=loop)
        return crd.mL2mH(msmc, alphas_mc, mc, crd.nfMmu, scale, loop)
    else:
        raise ValueError('Invalid input: f={}, scale={}'.format(f, scale))