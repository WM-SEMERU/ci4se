def find_max_label_length(labels):
    length = 0
    for i in range(len(labels)):
        if len(labels[i]) > length:
            length = len(labels[i])
    return length