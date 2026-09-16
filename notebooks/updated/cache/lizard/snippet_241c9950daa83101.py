def nrmse(test, ref, mask=None):
    test, ref, mask = _preprocess_input(test, ref, mask)
    if mask is not None:
        test = mask * test
        ref = mask * ref
    num = np.sqrt(mse(test, ref))
    deno = np.sqrt(np.mean(np.square(test)))
    return num / deno