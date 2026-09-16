def get_data_sklearn_format(train_file_list, module):
    data = list(readTrainingData(train_file_list, module.GROUP_LABEL))
    random.shuffle(data)
    x, y = [], []
    for raw_string, components in data:
        tokens, labels = zip(*components)
        x.append(raw_string)
        y.append(labels)
    return x, y