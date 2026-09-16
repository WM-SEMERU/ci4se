def major_axis(points):
    U, S, V = np.linalg.svd(points)
    axis = util.unitize(np.dot(S, V))
    return axis