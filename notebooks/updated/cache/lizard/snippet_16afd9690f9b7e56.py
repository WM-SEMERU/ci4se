def psnr(test, ref, mask=None):
    test, ref, mask = _preprocess_input(test, ref, mask)
    if mask is not None:
        test = mask * test
        ref = mask * ref
    num = np.max(np.abs(test))
    deno = mse(test, ref)
    return 10.0 * np.log10(num / deno)