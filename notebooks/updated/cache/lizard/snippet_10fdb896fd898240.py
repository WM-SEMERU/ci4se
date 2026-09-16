def face_ordering(mesh):
    norms = mesh.edges_unique_length[mesh.edges_unique_inverse].reshape((-1, 3)
        )
    small = norms.argmin(axis=1)
    MLidx = np.column_stack((small + 1, small + 2)) % 3
    MLidx += (np.arange(len(small)) * 3).reshape((-1, 1))
    diff = np.subtract(*norms.reshape(-1)[MLidx.T])
    order = np.zeros(len(norms), dtype=np.int64)
    order[diff < tol.merge] = -1
    order[diff > tol.merge] = 1
    return order