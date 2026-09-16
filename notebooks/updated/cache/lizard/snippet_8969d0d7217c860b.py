def GenerateHelpText(self, env, sort=None):
    if callable(sort):
        options = sorted(self.options, key=cmp_to_key(lambda x, y: sort(x.
            key, y.key)))
    elif sort is True:
        options = sorted(self.options, key=lambda x: x.key)
    else:
        options = self.options

    def format(opt, self=self, env=env):
        if opt.key in env:
            actual = env.subst('${%s}' % opt.key)
        else:
            actual = None
        return self.FormatVariableHelpText(env, opt.key, opt.help, opt.
            default, actual, opt.aliases)
    lines = [_f for _f in map(format, options) if _f]
    return ''.join(lines)