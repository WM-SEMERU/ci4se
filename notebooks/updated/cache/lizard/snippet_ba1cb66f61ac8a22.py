def rock(cls, data, eps, number_clusters, threshold=0.5, ccore=False):
    data = cls.input_preprocess(data)
    model = rock(data, eps, number_clusters, threshold, ccore)
    return cls(model)