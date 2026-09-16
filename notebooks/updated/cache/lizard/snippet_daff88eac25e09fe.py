def run_cm(cm, time_scale):
    cm = np.linalg.matrix_power(cm, time_scale)
    cm[cm > 1] = 1
    return cm