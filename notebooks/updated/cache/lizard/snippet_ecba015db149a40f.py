def pwm_array2pssm_array(arr, background_probs=DEFAULT_BASE_BACKGROUND):
    b = background_probs2array(background_probs)
    b = b.reshape([1, 4, 1])
    return np.log(arr / b).astype(arr.dtype)