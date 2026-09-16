def do_minus(self, parser, group):
    grouper = group.__class__()
    next_not = None
    for node in group:
        if isinstance(node, self.Minus):
            if next_not is not None:
                continue
            next_not = whoosh.qparser.syntax.NotGroup()
            grouper.append(next_not)
        else:
            if isinstance(node, whoosh.qparser.syntax.GroupNode):
                node = self.do_minus(parser, node)
            if next_not is not None:
                next_not.append(node)
                next_not = None
            else:
                grouper.append(node)
    if next_not is not None:
        grouper.pop()
    return grouper