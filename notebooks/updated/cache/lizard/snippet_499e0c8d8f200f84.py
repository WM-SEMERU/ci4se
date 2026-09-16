def visit_decorators(self, node):
    return '@%s\n' % '\n@'.join(item.accept(self) for item in node.nodes)