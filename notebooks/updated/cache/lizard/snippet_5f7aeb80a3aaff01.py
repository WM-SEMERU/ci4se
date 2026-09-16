def typecast(self, type_):
    self.value = SymbolTYPECAST.make_node(type_, self.value, self.lineno)
    return self.value is not None