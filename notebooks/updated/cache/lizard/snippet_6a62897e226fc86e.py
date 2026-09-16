def get_instance_variables(node, bound_name_classifier=
    BOUND_METHOD_ARGUMENT_NAME):
    node_attributes = [child for child in ast.walk(node) if isinstance(
        child, ast.Attribute) and get_attribute_name_id(child) ==
        bound_name_classifier]
    node_function_call_names = [get_object_name(child) for child in ast.
        walk(node) if isinstance(child, ast.Call)]
    node_instance_variables = [attribute for attribute in node_attributes if
        get_object_name(attribute) not in node_function_call_names]
    return node_instance_variables