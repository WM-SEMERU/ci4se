def consolidate(self, args):
    result = dict(args)
    for opt in self:
        if opt.name in result:
            result[opt.name] = opt.convert(result[opt.name])
        elif opt.default is not None:
            result[opt.name] = opt.convert(opt.default)
    return result