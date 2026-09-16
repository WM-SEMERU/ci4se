def calculate_reduce_output_shapes(operator):
    check_input_and_output_numbers(operator, input_count_range=1,
        output_count_range=1)
    check_input_and_output_types(operator, good_input_types=[FloatTensorType])
    output_shape = copy.deepcopy(operator.inputs[0].type.shape)
    params = operator.raw_operator.reduce
    from coremltools.proto.NeuralNetwork_pb2 import ReduceLayerParams as Params
    if params.axis in [Params.CHW, Params.C]:
        output_shape[1] = 1
    if params.axis in [Params.CHW, Params.HW, Params.H]:
        output_shape[2] = 1
    if params.axis in [Params.CHW, Params.HW, Params.W]:
        output_shape[3] = 1
    operator.outputs[0].type.shape = output_shape