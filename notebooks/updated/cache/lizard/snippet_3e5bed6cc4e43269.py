def uvw(self, context):
    (lt, ut), (la, ua), (l, u) = context.array_extents(context.name)
    data = np.empty(context.shape, context.dtype)
    data[:, :, (0)] = np.arange(la + 1, ua + 1)
    data[:, :, (1)] = 0
    data[:, :, (2)] = 0
    return data