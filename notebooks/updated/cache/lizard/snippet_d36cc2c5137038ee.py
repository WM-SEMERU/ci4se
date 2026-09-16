def relation_operation(self):
    if len(self.nodes) > 0:
        rel_op = self.nodes[-1].relation_operation
    else:
        rel_op = None
    return rel_op