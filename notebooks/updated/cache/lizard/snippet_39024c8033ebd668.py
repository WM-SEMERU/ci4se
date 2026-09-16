def convolveSpectrumSame(Omega, CrossSection, Resolution=0.1, AF_wing=10.0,
    SlitFunction=SLIT_RECTANGULAR):
    step = Omega[1] - Omega[0]
    x = arange(-AF_wing, AF_wing + step, step)
    slit = SlitFunction(x, Resolution)
    print('step=')
    print(step)
    print('x=')
    print(x)
    print('slitfunc=')
    print(SlitFunction)
    CrossSectionLowRes = convolve(CrossSection, slit, mode='same') * step
    return Omega, CrossSectionLowRes, None, None, slit