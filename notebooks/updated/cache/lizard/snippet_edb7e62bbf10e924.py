def evaluate_classifier(input_, labels, per_example_weights=None, topk=1,
    name=PROVIDED, phase=Phase.train):
    result = input_.evaluate_classifier_fraction(labels,
        per_example_weights=per_example_weights, topk=topk, name=name,
        phase=phase)
    return input_.with_tensor(result[0] / result[1], result.layer_parameters)