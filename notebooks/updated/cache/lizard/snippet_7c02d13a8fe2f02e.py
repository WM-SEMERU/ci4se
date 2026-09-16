def ser_iuwt_recomposition(in1, scale_adjust, smoothed_array):
    wavelet_filter = 1.0 / 16 * np.array([1, 4, 6, 4, 1])
    max_scale = in1.shape[0] + scale_adjust
    if smoothed_array is None:
        recomposition = np.zeros([in1.shape[1], in1.shape[2]])
    else:
        recomposition = smoothed_array
    for i in range(max_scale - 1, scale_adjust - 1, -1):
        recomposition = ser_a_trous(recomposition, wavelet_filter, i) + in1[(
            i - scale_adjust), :, :]
    if scale_adjust > 0:
        for i in range(scale_adjust - 1, -1, -1):
            recomposition = ser_a_trous(recomposition, wavelet_filter, i)
    return recomposition