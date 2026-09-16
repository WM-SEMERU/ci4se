def recover_partitioned_variable_map(var_node_map):
    offset_variables_map = {}
    for var_key, var_tensor in var_node_map.items():
        match, var_name, offset = _extract_variable_parts(var_key, var_tensor)
        if not match:
            if var_key in offset_variables_map:
                raise RuntimeError(
                    'Variable %s exists both as a single and partitioned variable.'
                    )
            offset_variables_map[var_key] = var_tensor
            continue
        if var_name not in offset_variables_map:
            offset_variables_map[var_name] = {}
        elif not isinstance(offset_variables_map[var_name], dict):
            raise RuntimeError(
                'Variable %s exists both as a single and partitioned variable.'
                )
        if offset in offset_variables_map[var_name]:
            raise RuntimeError(
                'Variable map contains duplicate offset %d for variable [%s]' %
                (offset, var_name))
        offset_variables_map[var_name][offset] = var_tensor
    variables_map = {}
    for var_name, var_value in offset_variables_map.items():
        if not isinstance(var_value, dict):
            variables_map[var_name] = var_value
            continue
        shapes = [var_tensor.shape[1:] for var_tensor in var_value.values()]
        if not all(shape == shapes[0] for shape in shapes):
            raise RuntimeError('Shapes not compatible: %s' % shapes)
        for _, tensor in sorted(var_value.items()):
            variables_map[var_name] = [tensor for _, tensor in sorted(
                var_value.items())]
    return variables_map