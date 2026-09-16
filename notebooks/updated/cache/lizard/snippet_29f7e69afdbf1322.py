def evalHeatKernel(dgm1, dgm2, sigma):
    kSigma = 0
    I1 = np.array(dgm1)
    I2 = np.array(dgm2)
    for i in range(I1.shape[0]):
        p = I1[(i), 0:2]
        for j in range(I2.shape[0]):
            q = I2[(j), 0:2]
            qc = I2[(j), 1::-1]
            kSigma += np.exp(-np.sum((p - q) ** 2) / (8 * sigma)) - np.exp(
                -np.sum((p - qc) ** 2) / (8 * sigma))
    return kSigma / (8 * np.pi * sigma)