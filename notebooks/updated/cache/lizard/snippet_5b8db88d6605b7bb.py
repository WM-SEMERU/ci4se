def is_flask_route_function(ast_node):
    for decorator in ast_node.decorator_list:
        if isinstance(decorator, ast.Call):
            if _get_last_of_iterable(get_call_names(decorator.func)
                ) == 'route':
                return True
    return False