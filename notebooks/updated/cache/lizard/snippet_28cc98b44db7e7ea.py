def Softmax(a):
    e = np.exp(a)
    return np.divide(e, np.sum(e, axis=-1, keepdims=True)),