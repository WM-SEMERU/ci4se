def load_corpus(path):
    if not os.path.exists(path):
        raise ValueError(
            "'{}' dataset has not been downloaded, use the yellowbrick.download module to fetch datasets"
            .format(path))
    categories = [cat for cat in os.listdir(path) if os.path.isdir(os.path.
        join(path, cat))]
    files = []
    data = []
    target = []
    for cat in categories:
        for name in os.listdir(os.path.join(path, cat)):
            files.append(os.path.join(path, cat, name))
            target.append(cat)
            with open(os.path.join(path, cat, name), 'r') as f:
                data.append(f.read())
    return Bunch(categories=categories, files=files, data=data, target=target)