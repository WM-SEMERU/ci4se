def read_pos_neg_data(path, folder, limit):
    training_pos_path = os.path.join(path, folder, 'pos')
    training_neg_path = os.path.join(path, folder, 'neg')
    X_pos = read_folder(training_pos_path)
    X_neg = read_folder(training_neg_path)
    if limit is None:
        X = X_pos + X_neg
    else:
        X = X_pos[:limit] + X_neg[:limit]
    y = [1] * int(len(X) / 2) + [0] * int(len(X) / 2)
    return X, y