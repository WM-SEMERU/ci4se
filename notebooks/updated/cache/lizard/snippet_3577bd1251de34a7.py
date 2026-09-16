def se(actual, predicted):
    return np.power(np.array(actual) - np.array(predicted), 2)