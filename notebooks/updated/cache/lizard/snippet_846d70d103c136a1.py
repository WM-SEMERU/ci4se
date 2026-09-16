def load_boston():
    dataset = datasets.load_boston()
    return Dataset(load_boston.__doc__, dataset.data, dataset.target, r2_score)