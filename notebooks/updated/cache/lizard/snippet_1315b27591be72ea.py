def ci2ls(ci):
    if not np.size(ci):
        return ci
    _, ci = np.unique(ci, return_inverse=True)
    ci += 1
    nr_indices = int(max(ci))
    ls = []
    for c in range(nr_indices):
        ls.append([])
    for i, x in enumerate(ci):
        ls[ci[i] - 1].append(i)
    return ls