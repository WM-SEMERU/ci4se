def p_joinx(self, t):
    if len(t) == 4:
        t[0] = JoinX(t[1], t[3], None, t[2])
    elif len(t) == 6:
        t[0] = JoinX(t[1], t[3], t[5], t[2])
    else:
        raise NotImplementedError('todo: join .. using')