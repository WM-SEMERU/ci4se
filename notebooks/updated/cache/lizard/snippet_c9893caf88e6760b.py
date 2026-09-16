def r2_score_vec(y_true, y_pred):
    numerator = (y_true - y_pred) ** 2
    denominator = (y_true - np.average(y_true)) ** 2
    nonzero_denominator = denominator != 0
    nonzero_numerator = numerator != 0
    valid_score = nonzero_denominator & nonzero_numerator
    output_scores = np.ones([y_true.shape[0]])
    output_scores[valid_score] = 1 - numerator[valid_score] / denominator[
        valid_score]
    output_scores[nonzero_numerator & ~nonzero_denominator] = 0.0
    return output_scores