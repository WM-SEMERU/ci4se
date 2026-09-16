def calculate_feature_vectorizer_output_shapes(operator):
    check_input_and_output_numbers(operator, input_count_range=[1, None],
        output_count_range=1)
    check_input_and_output_types(operator, good_input_types=[
        FloatTensorType, Int64TensorType, FloatType, Int64Type])
    if any(len(variable.type.shape) != 2 for variable in operator.inputs):
        raise RuntimeError('Input(s) must be 2-D tensor(s)')
    N = 'None'
    for variable in operator.inputs:
        if variable.type.shape[0] != 'None':
            N = variable.type.shape[0]
            break
    for variable in operator.inputs:
        if variable.type.shape[0] not in ['None', N]:
            raise RuntimeError(
                'The batch dimensions should be the same to all input tensors.'
                )
    C = sum(info.inputDimensions for info in operator.raw_operator.
        featureVectorizer.inputList)
    doc_string = operator.outputs[0].type.doc_string
    if all(isinstance(variable.type, (Int64TensorType, Int64Type)) for
        variable in operator.inputs):
        operator.outputs[0].type = Int64TensorType([N, C], doc_string=
            doc_string)
    elif isinstance(operator.inputs[0].type, (FloatTensorType, FloatType)):
        operator.outputs[0].type = FloatTensorType([N, C], doc_string=
            doc_string)
    else:
        raise ValueError('Unsupported input type: %s' % type(operator.
            inputs[0].type))