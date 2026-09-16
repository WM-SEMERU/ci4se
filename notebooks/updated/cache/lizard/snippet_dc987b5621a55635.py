def build_output_map(protomap, get_tensor_by_name):

    def get_output_from_tensor_info(tensor_info):
        encoding = tensor_info.WhichOneof('encoding')
        if encoding == 'name':
            return get_tensor_by_name(tensor_info.name)
        elif encoding == 'coo_sparse':
            return tf.SparseTensor(get_tensor_by_name(tensor_info.
                coo_sparse.indices_tensor_name), get_tensor_by_name(
                tensor_info.coo_sparse.values_tensor_name),
                get_tensor_by_name(tensor_info.coo_sparse.
                dense_shape_tensor_name))
        else:
            raise ValueError('Invalid TensorInfo.encoding: %s' % encoding)
    return {key: get_output_from_tensor_info(tensor_info) for key,
        tensor_info in protomap.items()}