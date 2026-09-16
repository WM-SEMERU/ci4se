def visit_Call(self, node):
    if node in self.potential_iterator:
        matched_path = self.find_matching_builtin(node)
        if matched_path is None:
            return self.generic_visit(node)
        if matched_path[1] == 'map' and MODULES['__builtin__']['None'
            ] in self.aliases[node.args[0]]:
            return self.generic_visit(node)
        if matched_path[1] in ('array', 'asarray') and len(node.args) != 1:
            return self.generic_visit(node)
        path = EQUIVALENT_ITERATORS[matched_path]
        if path:
            node.func = path_to_attr(path)
            self.use_itertools |= path[0] == 'itertools'
        else:
            node = node.args[0]
        self.update = True
    return self.generic_visit(node)