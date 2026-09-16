def set_regressor_interface_params(spec, features, output_features):
    if output_features is None:
        output_features = [('predicted_class', datatypes.Double())]
    else:
        output_features = _fm.process_or_validate_features(output_features, 1)
    if len(output_features) != 1:
        raise ValueError(
            'Provided output features for a regressor must be one Double feature.'
            )
    if output_features[0][1] != datatypes.Double():
        raise ValueError('Output type of a regressor must be a Double.')
    prediction_name = output_features[0][0]
    spec.description.predictedFeatureName = prediction_name
    features = _fm.process_or_validate_features(features)
    for cur_input_name, feature_type in features:
        input_ = spec.description.input.add()
        input_.name = cur_input_name
        datatypes._set_datatype(input_.type, feature_type)
    output_ = spec.description.output.add()
    output_.name = prediction_name
    datatypes._set_datatype(output_.type, 'Double')
    return spec