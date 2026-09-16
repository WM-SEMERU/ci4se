def _jmomentsurfaceIntegrand(vz, vR, vT, R, z, df, sigmaR1, gamma, sigmaz1,
    n, m, o):
    return df(R, vR * sigmaR1, vT * sigmaR1 * gamma, z, vz * sigmaz1,
        use_physical=False, func=lambda x, y, z: x ** n * y ** m * z ** o)