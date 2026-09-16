def operator(self, lhs, min_precedence):
    while self.accept_operator(precedence=min_precedence):
        operator = self.tokens.matched.operator
        if operator.suffix:
            rhs = self.expression()
            self.tokens.expect(common_grammar.match_tokens(operator.suffix))
            rhs.end = self.tokens.matched.end
        elif operator.name == '.':
            rhs = self.dot_rhs()
        else:
            rhs = self.atom()
        next_min_precedence = operator.precedence
        if operator.assoc == 'left':
            next_min_precedence += 1
        while self.tokens.match(grammar.infix):
            if self.tokens.matched.operator.precedence < next_min_precedence:
                break
            rhs = self.operator(rhs, self.tokens.matched.operator.precedence)
        lhs = operator.handler(lhs, rhs, start=lhs.start, end=rhs.end,
            source=self.original)
    return lhs