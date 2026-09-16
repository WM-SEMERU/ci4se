def get_integrated_act(x, axis=0, window=50, fast=False):
    f = get_acf(x, axis=axis, fast=fast)
    if len(f.shape) == 1:
        return 1 + 2 * np.sum(f[1:window])
    m = [slice(None)] * len(f.shape)
    m[axis] = slice(1, window)
    tau = 1 + 2 * np.sum(f[tuple(m)], axis=axis)
    return tau