def p_param_types(self, p):
    if len(p) == 2:
        p[0] = tuple((t,) for t in p[1])
    elif len(p) == 3:
        p[0] = tuple((t,) for t in p[1]) + ((),)
    elif len(p) == 4:
        p[0] = tuple((t,) + ts for t in p[1] for ts in p[3])
    else:
        non_defaults = [t for t in p[4] if len(t) == len(p[4][0])]
        p[0] = tuple((t,) + ts for t in p[1] for ts in non_defaults) + p[4]