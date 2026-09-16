def add_symbol(self, name, string=None):
    if not string:
        string = name
    self.symbols[name] = sympy.Symbol(string)