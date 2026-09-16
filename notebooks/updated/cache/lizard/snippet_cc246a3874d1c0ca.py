def _fft_convolve_gpu(data_g, h_g, res_g=None, plan=None, inplace=False,
    kernel_is_fft=False):
    assert_bufs_type(np.complex64, data_g, h_g)
    if data_g.shape != h_g.shape:
        raise ValueError('data and kernel must have same size! %s vs %s ' %
            (str(data_g.shape), str(h_g.shape)))
    if plan is None:
        plan = fft_plan(data_g.shape)
    if inplace:
        res_g = data_g
    else:
        if res_g is None:
            res_g = OCLArray.empty(data_g.shape, data_g.dtype)
        res_g.copy_buffer(data_g)
    if not kernel_is_fft:
        kern_g = OCLArray.empty(h_g.shape, h_g.dtype)
        kern_g.copy_buffer(h_g)
        fft(kern_g, inplace=True, plan=plan)
    else:
        kern_g = h_g
    fft(res_g, inplace=True, plan=plan)
    _complex_multiply_kernel(res_g, kern_g)
    fft(res_g, inplace=True, inverse=True, plan=plan)
    return res_g