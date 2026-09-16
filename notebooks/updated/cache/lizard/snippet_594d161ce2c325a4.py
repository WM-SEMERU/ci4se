def visit_classdef(self, node, parent, newstyle=None):
    node, doc = self._get_doc(node)
    newnode = nodes.ClassDef(node.name, doc, node.lineno, node.col_offset,
        parent)
    metaclass = None
    if PY3:
        for keyword in node.keywords:
            if keyword.arg == 'metaclass':
                metaclass = self.visit(keyword, newnode).value
                break
    if node.decorator_list:
        decorators = self.visit_decorators(node, newnode)
    else:
        decorators = None
    newnode.postinit([self.visit(child, newnode) for child in node.bases],
        [self.visit(child, newnode) for child in node.body], decorators,
        newstyle, metaclass, [self.visit(kwd, newnode) for kwd in node.
        keywords if kwd.arg != 'metaclass'] if PY3 else [])
    return newnode