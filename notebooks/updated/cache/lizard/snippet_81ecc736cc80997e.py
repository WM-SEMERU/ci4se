def parse_declaration_expressn_tupleliteral(self, values, es):
    es = es + '('
    for ast in values:
        es = es + self.parse_declaration_expressn(ast, es='') + ', '
    if es.endswith(', '):
        es = es[:-2]
    return es + ')'