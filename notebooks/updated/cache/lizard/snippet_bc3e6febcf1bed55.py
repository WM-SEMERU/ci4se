def visit_Name(self, node):
    if node.id in self.symbols:
        symbol = path_to_node(self.symbols[node.id])
        if not getattr(symbol, 'isliteral', lambda : False)():
            parent = self.ancestors[node][-1]
            blacklist = ast.Tuple, ast.List, ast.Set, ast.Return
            if isinstance(parent, blacklist):
                raise PythranSyntaxError(
                    'Unsupported module identifier manipulation', node)
        new_node = path_to_attr(self.symbols[node.id])
        new_node.ctx = node.ctx
        ast.copy_location(new_node, node)
        return new_node
    return node