def cdfNormal(z):
    if abs(z) < ERF_CODY_LIMIT1:
        return 0.5 * (1.0 + z / M_SQRT2 * _erfRationalHelperR3(0.5 * z * z))
    elif z < 0.0:
        return np.exp(logPdfNormal(z)) * _erfRationalHelper(-z) / -z
    else:
        return 1.0 - np.exp(logPdfNormal(z)) * _erfRationalHelper(z) / z