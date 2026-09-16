def _vmomentsurfaceIntegrand(vR, vT, R, az, df, n, m, sigmaR1, sigmaT1, t,
    initvmoment):
    o = Orbit([R, vR * sigmaR1, vT * sigmaT1, az])
    return vR ** n * vT ** m * df(o, t) / initvmoment