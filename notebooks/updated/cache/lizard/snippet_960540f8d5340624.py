def damping_kraus_map(p=0.1):
    damping_op = np.sqrt(p) * np.array([[0, 1], [0, 0]])
    residual_kraus = np.diag([1, np.sqrt(1 - p)])
    return [residual_kraus, damping_op]