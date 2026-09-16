def get_functions(self):
    instances = self._get_instances(ast.FunctionDef)
    instances = [PyFunction(instance, self.package) for instance in instances]
    return instances