def apply_threshold(in1, threshold, sigma_level=4):
    out1 = np.empty_like(in1)
    if len(in1.shape) == 2:
        out1 = (np.abs(in1) > sigma_level * threshold) * in1
    else:
        for i in range(in1.shape[0]):
            out1[(i), :, :] = (np.abs(in1[(i), :, :]) > sigma_level *
                threshold[i]) * in1[(i), :, :]
    return out1