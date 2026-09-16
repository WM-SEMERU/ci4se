def as_spinor_array(a):
    a = np.atleast_1d(a)
    assert a.dtype == np.dtype(np.quaternion)
    return a.view(np.float).reshape(a.shape + (4,))[..., [0, 3, 2, 1]].ravel(
        ).view(np.complex).reshape(a.shape + (2,))