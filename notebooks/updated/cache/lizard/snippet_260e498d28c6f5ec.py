def proppivot(self, prop):
    pval = s_ast.RelPropValue(kids=(prop,))
    self.ignore(whitespace)
    self.nextmust('->')
    self.ignore(whitespace)
    if self.nextchar() == '*':
        self.offs += 1
        return s_ast.PropPivotOut(kids=(prop,))
    dest = self.absprop()
    return s_ast.PropPivot(kids=(pval, dest))