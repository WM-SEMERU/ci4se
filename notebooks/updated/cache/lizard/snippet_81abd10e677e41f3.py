def contains(self, assertion):
    if not isinstance(assertion, IndependenceAssertion):
        raise TypeError(
            "' in <Independencies()>' requires IndependenceAssertion" +
            ' as left operand, not {0}'.format(type(assertion)))
    return assertion in self.get_assertions()