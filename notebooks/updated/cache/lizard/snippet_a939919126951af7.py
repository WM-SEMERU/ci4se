def evaluate_classifier_fraction_sparse(input_, labels, per_example_weights
    =None, topk=1, name=PROVIDED, phase=Phase.train):
    _ = name
    if not (tf.int32.is_compatible_with(labels.dtype) or tf.int64.
        is_compatible_with(labels.dtype)):
        raise ValueError('Labels must be an integer type.: %s.' % labels.dtype)
    correct_predictions, examples = _compute_sparse_average_correct(input_,
        labels, per_example_weights, topk=topk)
    correct_predictions, examples, my_parameters = _eval_metric(input_,
        topk, correct_predictions, examples, phase)
    return input_.with_sequence([correct_predictions, examples], my_parameters)