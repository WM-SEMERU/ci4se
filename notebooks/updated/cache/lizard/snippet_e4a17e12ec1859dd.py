def grouped(self):
    collection = OrderedDict(_=Args(no_argv=True))
    _current_group = None
    for arg in self.all:
        if arg.startswith('-'):
            _current_group = arg
            collection.setdefault(arg, Args(no_argv=True))
        elif _current_group:
            collection[_current_group]._args.append(arg)
        else:
            collection['_']._args.append(arg)
    return collection