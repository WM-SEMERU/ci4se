def psnr_stack(data1, data2, metric=np.mean, method='starck'):
    r
    if data1.ndim != 3 or data2.ndim != 3:
        raise ValueError('Input data must be a 3D np.ndarray')
    return metric([psnr(i, j, method=method) for i, j in zip(data1, data2)])