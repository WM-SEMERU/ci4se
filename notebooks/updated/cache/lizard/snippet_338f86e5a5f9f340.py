def check_register(self, arg):
    self.check_parameter(arg)
    match = re.search(self.REGISTER_REGEX, arg)
    if match is None:
        raise iarm.exceptions.RuleError('Parameter {} is not a register'.
            format(arg))
    try:
        r_num = int(match.groups()[0])
    except ValueError:
        r_num = int(match.groups()[0], 16)
    except TypeError:
        if arg in 'lr|LR':
            return 14
        elif arg in 'sp|SP':
            return 13
        elif arg in 'fp|FP':
            return 7
        else:
            raise
    if r_num > self._max_registers:
        raise iarm.exceptions.RuleError(
            'Register {} is greater than defined registers of {}'.format(
            arg, self._max_registers))
    return r_num