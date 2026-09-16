def visit_oper(self, node, _):
    oper = node.text
    if oper == ':':
        oper = '='
    return oper