def get_version():
    import ast
    with open(os.path.join('cyvcf2', '__init__.py'), 'r') as init_file:
        module = ast.parse(init_file.read())
    version = (ast.literal_eval(node.value) for node in ast.walk(module) if
        isinstance(node, ast.Assign) and node.targets[0].id == '__version__')
    try:
        return next(version)
    except StopIteration:
        raise ValueError('version could not be located')