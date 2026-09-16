def argrelmin(data, axis=0, order=1, mode='clip'):
    return argrelextrema(data, np.less, axis, order, mode)