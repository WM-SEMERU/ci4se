def visit_Import(self, node):
    for alias in node.names:
        current_module = MODULES
        for path in alias.name.split('.'):
            if path not in current_module:
                raise PythranSyntaxError("Module '{0}' unknown.".format(
                    alias.name), node)
            else:
                current_module = current_module[path]