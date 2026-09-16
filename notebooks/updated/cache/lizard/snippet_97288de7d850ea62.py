def hellinger_distance(outputs, targets, derivative=False):
    root_difference = np.sqrt(outputs) - np.sqrt(targets)
    if derivative:
        return root_difference / (np.sqrt(2) * np.sqrt(outputs))
    else:
        return np.mean(np.sum(np.power(root_difference, 2), axis=1) / math.
            sqrt(2))