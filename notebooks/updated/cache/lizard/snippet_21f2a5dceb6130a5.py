def ParseArgs(self, args):
    for descriptor in self:
        value = args.pop(descriptor.name, None)
        if value is None:
            value = descriptor.default
        else:
            try:
                value = descriptor.Validate(value)
            except Exception:
                logging.error('Invalid value %s for arg %s', value,
                    descriptor.name)
                raise
        yield descriptor.name, value