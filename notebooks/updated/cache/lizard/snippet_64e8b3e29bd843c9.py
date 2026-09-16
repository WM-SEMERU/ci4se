def visit_Identifier(self, node):
    if not self._is_mangle_candidate(node):
        return
    name = node.value
    symbol = node.scope.resolve(node.value)
    if symbol is None:
        return
    mangled = symbol.scope.mangled.get(name)
    if mangled is not None:
        node.value = mangled