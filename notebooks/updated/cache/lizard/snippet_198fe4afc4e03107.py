def dct2(input, K=13):
    nframes, N = input.shape
    freqstep = numpy.pi / N
    cosmat = dctmat(N, K, freqstep, False)
    return numpy.dot(input, cosmat) * (2.0 / N)