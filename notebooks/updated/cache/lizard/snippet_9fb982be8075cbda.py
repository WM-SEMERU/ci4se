def get(self, symbol):
    syms = self.try_to_get(symbol)
    if syms is None:
        raise Exception('Symbol {} does not exist'.format(symbol))
    else:
        return syms