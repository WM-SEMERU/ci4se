def entropy(dictionary):
    total = 0.0
    entropy = 0
    for key in dictionary.keys():
        total += dictionary[key]
    for key in dictionary.keys():
        entropy += dictionary[key] / total * log(1.0 / (dictionary[key] /
            total), 2)
    return entropy