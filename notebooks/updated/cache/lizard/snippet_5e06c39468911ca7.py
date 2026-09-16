def evaluate(self, scope, local_vars, block=None):
    method = self.compiled_method(local_vars.keys())
    setattr(scope, 'compiled', method)
    return scope.compiled(local_vars, block=block)