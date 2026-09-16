def p_kw_args_update(self, p):
    p[0] = p[1]
    for key in p[3]:
        if key in p[1]:
            msg = "Keyword argument '%s' defined more than once." % key
            self.errors.append((msg, p.lineno(2), self.path))
    p[0].update(p[3])