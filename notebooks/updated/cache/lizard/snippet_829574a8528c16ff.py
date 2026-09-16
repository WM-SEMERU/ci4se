def is_probably_builtin(node):
    prev = node.prev_sibling
    if prev is not None and prev.type == token.DOT:
        return False
    parent = node.parent
    if parent.type in (syms.funcdef, syms.classdef):
        return False
    if parent.type == syms.expr_stmt and parent.children[0] is node:
        return False
    if (parent.type == syms.parameters or parent.type == syms.typedargslist and
        (prev is not None and prev.type == token.COMMA or parent.children[0
        ] is node)):
        return False
    return True