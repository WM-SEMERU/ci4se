def load_newsgroups():
    dataset = datasets.fetch_20newsgroups()
    return Dataset(load_newsgroups.__doc__, np.array(dataset.data), dataset
        .target, accuracy_score, stratify=True)