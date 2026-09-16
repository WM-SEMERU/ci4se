def irfft(a, n=None, axis=-1, norm=None):
    output = mkl_fft.irfft_numpy(a, n=n, axis=axis)
    if _unitary(norm):
        output *= sqrt(output.shape[axis])
    return output