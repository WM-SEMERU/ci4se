def transDrift(length=0.0, gamma=None):
    m = np.eye(6, 6, dtype=np.float64)
    if length == 0.0:
        print("warning: 'length' should be a positive float number.")
    elif gamma is not None and gamma != 0.0:
        m[0, 1] = m[2, 3] = length
        m[4, 5] = float(length) / gamma / gamma
    else:
        print("warning: 'gamma' should be a positive float number.")
    return m