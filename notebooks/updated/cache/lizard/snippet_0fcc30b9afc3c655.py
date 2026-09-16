def identity_on_pols(self, context):
    A = np.empty(context.shape, context.dtype)
    A[:, :, :] = [[[1, 0, 0, 1]]]
    return A