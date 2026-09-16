def _get_verts_and_connect(self, paths):
    verts = np.vstack(paths)
    gaps = np.add.accumulate(np.array([len(x) for x in paths])) - 1
    connect = np.ones(gaps[-1], dtype=bool)
    connect[gaps[:-1]] = False
    return verts, connect