def edge(self, c):
    return ca.logic_and(c, ca.logic_not(self.pre_cond(c)))