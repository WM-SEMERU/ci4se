def normalize_mesh(mesh):
    mesh = dict(mesh)
    pos = mesh['position'][:, :3].copy()
    pos -= (pos.max(0) + pos.min(0)) / 2.0
    pos /= np.abs(pos).max()
    mesh['position'] = pos
    return mesh