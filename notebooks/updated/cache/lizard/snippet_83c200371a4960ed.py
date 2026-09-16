def p_jointype(self, t):
    if len(t) <= 2 or t[1] == 'inner':
        t[0] = JoinTypeX(None, False, None)
    else:
        t[0] = JoinTypeX(t[1], True, None)