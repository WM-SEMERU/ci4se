def check_first_party_caveat(self, ctx, cav):
    try:
        cond, arg = parse_caveat(cav)
    except ValueError as ex:
        return 'cannot parse caveat "{}": {}'.format(cav, ex.args[0])
    checker = self._checkers.get(cond)
    if checker is None:
        return 'caveat "{}" not satisfied: caveat not recognized'.format(cav)
    err = checker.check(ctx, cond, arg)
    if err is not None:
        return 'caveat "{}" not satisfied: {}'.format(cav, err)