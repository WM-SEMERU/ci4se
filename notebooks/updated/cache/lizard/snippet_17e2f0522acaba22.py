def m_c(mcmc, scale, f, alphasMZ=0.1185, loop=3):
    r
    if scale == mcmc:
        return mcmc
    _sane(scale, f)
    crd = rundec.CRunDec()
    alphas_mc = alpha_s(mcmc, 4, alphasMZ=alphasMZ, loop=loop)
    if f == 4:
        alphas_scale = alpha_s(scale, f, alphasMZ=alphasMZ, loop=loop)
        return crd.mMS2mMS(mcmc, alphas_mc, alphas_scale, f, loop)
    elif f == 3:
        crd.nfMmu.Mth = 1.3
        crd.nfMmu.muth = 1.3
        crd.nfMmu.nf = 4
        return crd.mH2mL(mcmc, alphas_mc, mcmc, crd.nfMmu, scale, loop)
    elif f == 5:
        crd.nfMmu.Mth = 4.8
        crd.nfMmu.muth = 4.8
        crd.nfMmu.nf = 5
        return crd.mL2mH(mcmc, alphas_mc, mcmc, crd.nfMmu, scale, loop)
    else:
        raise ValueError('Invalid input: f={}, scale={}'.format(f, scale))