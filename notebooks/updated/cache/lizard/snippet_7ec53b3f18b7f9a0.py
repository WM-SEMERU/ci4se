def bind(self, f):

    @Parser
    def _bind(tokens, s):
        v, s2 = self.run(tokens, s)
        return f(v).run(tokens, s2)
    _bind.name = '(%s >>=)' % (self.name,)
    return _bind