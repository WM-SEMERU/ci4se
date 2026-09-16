def p_andnode_expression(self, t):
    self.accu.add(Term('vertex', ['and("' + t[2] + '")']))
    t[0] = 'and("' + t[2] + '")'