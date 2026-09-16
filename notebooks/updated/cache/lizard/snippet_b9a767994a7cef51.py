def has_dynamic_getattr(self, context=None):

    def _valid_getattr(node):
        root = node.root()
        return root.name != BUILTINS and getattr(root, 'pure_python', None)
    try:
        return _valid_getattr(self.getattr('__getattr__', context)[0])
    except exceptions.AttributeInferenceError:
        try:
            getattribute = self.getattr('__getattribute__', context)[0]
            return _valid_getattr(getattribute)
        except exceptions.AttributeInferenceError:
            pass
    return False