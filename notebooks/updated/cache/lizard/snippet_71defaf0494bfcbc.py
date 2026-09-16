def get_normalized_variable_map(scope_or_module, collection=tf.GraphKeys.
    GLOBAL_VARIABLES, context=None, group_sliced_variables=True):
    scope_name = get_variable_scope_name(scope_or_module)
    if context is None:
        context = scope_or_module
    prefix = get_variable_scope_name(context)
    prefix_length = len(prefix) + 1 if prefix else 0
    if not _is_scope_prefix(scope_name, prefix):
        raise ValueError("Scope '{}' is not prefixed by '{}'.".format(
            scope_name, prefix))
    variables = get_variables_in_scope(scope_name, collection)
    if not group_sliced_variables:
        single_vars = variables
        grouped_vars = dict()
    else:
        single_vars, grouped_vars = _get_sliced_variables(variables)
    var_map = {var.op.name[prefix_length:]: var for var in single_vars}
    for full_name, var_group in grouped_vars.items():
        name = full_name[prefix_length:]
        if name in var_map:
            raise ValueError(
                'Mixing slices and non-slices with the same name: ' + str(name)
                )
        var_map[name] = var_group
    return var_map