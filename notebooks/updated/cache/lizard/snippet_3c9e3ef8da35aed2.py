def in_array_list(array_list, a, tol=1e-05):
    if len(array_list) == 0:
        return False
    axes = tuple(range(1, a.ndim + 1))
    if not tol:
        return np.any(np.all(np.equal(array_list, a[(None), :]), axes))
    else:
        return np.any(np.sum(np.abs(array_list - a[(None), :]), axes) < tol)