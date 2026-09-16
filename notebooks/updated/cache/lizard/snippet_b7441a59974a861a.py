def compute_jaccard_index(x_set, y_set):
    if not x_set or not y_set:
        return 0.0
    intersection_cardinal = len(x_set & y_set)
    union_cardinal = len(x_set | y_set)
    return intersection_cardinal / float(union_cardinal)