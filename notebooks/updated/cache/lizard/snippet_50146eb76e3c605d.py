def table_r_node(self, node):
    start = len(self.f.getvalue())
    try:
        self.default(node)
    except GenericASTTraversalPruningException:
        final = len(self.f.getvalue())
        self.set_pos_info(node, start, final)
        self.set_pos_info(node[-1], start, final)
        raise GenericASTTraversalPruningException