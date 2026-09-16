def set_model_version(model, version):
    if model is None or not isinstance(model, onnx_proto.ModelProto):
        raise ValueError('Model is not a valid ONNX model.')
    if not convert_utils.is_numeric_type(version):
        raise ValueError('Version must be a numeric type.')
    model.model_version = version