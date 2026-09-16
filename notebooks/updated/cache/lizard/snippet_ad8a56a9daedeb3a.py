def func(self):
    self.eat(TokenTypes.FUNC)
    name = Var(self.cur_token)
    self.eat(TokenTypes.VAR)
    self.eat(TokenTypes.LPAREN)
    sig = self.param_list()
    self.eat(TokenTypes.RPAREN)
    block = self.block()
    return FunctionDef(name, Function(sig, block))