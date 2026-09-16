def ijk_jlk_to_il(A, B):
    res = np.zeros((A.shape[0], B.shape[1]))
    [np.add(np.dot(A[:, :, (k)], B[:, :, (k)]), res, out=res) for k in
        range(B.shape[-1])]
    return res