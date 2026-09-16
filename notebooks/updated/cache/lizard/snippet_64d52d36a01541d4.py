def false_negatives(y, y_pred):
    y, y_pred = convert_assert(y, y_pred)
    assert_binary_problem(y)
    return np.count_nonzero(y_pred[y == 1] == 0)