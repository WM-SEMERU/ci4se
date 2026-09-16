def get_kind(self):
    scope = self.parent.get_scope()
    if isinstance(self.parent, PyClass):
        for decorator in self.decorators:
            pyname = rope.base.evaluate.eval_node(scope, decorator)
            if pyname == rope.base.builtins.builtins['staticmethod']:
                return 'staticmethod'
            if pyname == rope.base.builtins.builtins['classmethod']:
                return 'classmethod'
        return 'method'
    return 'function'