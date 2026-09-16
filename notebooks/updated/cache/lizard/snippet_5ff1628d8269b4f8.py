def ce(actual, predicted):
    return sum([(1.0) for x, y in zip(actual, predicted) if x != y]) / len(
        actual)