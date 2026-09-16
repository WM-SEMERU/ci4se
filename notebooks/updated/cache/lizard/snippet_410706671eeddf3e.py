def strel_pair(x, y):
    x_center = int(np.abs(x))
    y_center = int(np.abs(y))
    result = np.zeros((y_center * 2 + 1, x_center * 2 + 1), bool)
    result[y_center, x_center] = True
    result[y_center + int(y), x_center + int(x)] = True
    return result