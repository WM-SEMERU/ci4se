def find_best_question(X, y, criterion):
    measure_impurity = gini_impurity if criterion == 'gini' else entropy
    current_impurity = measure_impurity(y)
    best_info_gain = 0
    best_question = None
    for feature_n in range(X.shape[1]):
        for value in set(X[:, (feature_n)]):
            q = Question(feature_n, value)
            _, _, true_y, false_y = split(X, y, q)
            current_info_gain = info_gain(current_impurity, true_y, false_y,
                criterion)
            if current_info_gain >= best_info_gain:
                best_info_gain = current_info_gain
                best_question = q
    return best_info_gain, best_question