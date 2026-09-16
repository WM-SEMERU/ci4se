def _looks_like_numpy_function(func_name, numpy_module_name, node):
    return node.name == func_name and node.parent.name == numpy_module_name