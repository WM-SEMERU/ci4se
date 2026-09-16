def convolve_sep3(data, hx, hy, hz, res_g=None, sub_blocks=(1, 1, 1), tmp_g
    =None):
    if isinstance(data, np.ndarray):
        data = np.ascontiguousarray(data)
        if sub_blocks == (1, 1, 1) or sub_blocks is None:
            return _convolve_sep3_numpy(data, hx, hy, hz)
        else:
            N_sub = [int(np.ceil(1.0 * n / s)) for n, s in zip(data.shape,
                sub_blocks)]
            Npads = [int(len(_h) / 2) for _h in [hz, hy, hx]]
            res = np.empty(data.shape, np.float32)
            for i, (data_tile, data_s_src, data_s_dest) in enumerate(
                tile_iterator(data, blocksize=N_sub, padsize=Npads, mode=
                'constant')):
                res_tile = _convolve_sep3_numpy(data_tile.copy(), hx, hy, hz)
                res[data_s_src] = res_tile[data_s_dest]
            return res
    elif isinstance(data, OCLArray):
        return _convolve_sep3_gpu(data, hx, hy, hz, res_g=res_g, tmp_g=tmp_g)
    else:
        raise TypeError('array argument (1) has bad type: %s' % type(data))