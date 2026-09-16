def add_signature(key, inputs, outputs):
    _check_dict_maps_to_tensors_or_sparse_tensors(inputs)
    _check_dict_maps_to_tensors_or_sparse_tensors(outputs)
    input_info = {input_name: tf_v1.saved_model.utils.build_tensor_info(
        tensor) for input_name, tensor in inputs.items()}
    output_info = {output_name: tf_v1.saved_model.utils.build_tensor_info(
        tensor) for output_name, tensor in outputs.items()}
    signature = tf_v1.saved_model.signature_def_utils.build_signature_def(
        input_info, output_info)
    tf_v1.add_to_collection(_SIGNATURE_COLLECTION, (key, signature))