def _initialize(self, *args, **kwargs):
    self.items = None
    self.keys = None
    self.values = None
    if args:
        if len(args) != 2:
            raise TypeError(
                'expected exactly two positional arguments, got %s' % len(args)
                )
        if kwargs:
            raise TypeError(
                'expected positional or keyword arguments, not both')
        self.keys, self.values = map(self._validate_argument, args)
    elif kwargs:
        has_kv = 'keys' in kwargs and 'values' in kwargs
        has_of = 'of' in kwargs
        if not (has_kv or has_of):
            raise TypeError(
                'expected keys/values or items matchers, but got: %s' %
                list(kwargs.keys()))
        if has_kv and has_of:
            raise TypeError(
                'expected keys & values, or items matchers, not both')
        if has_kv:
            self.keys = self._validate_argument(kwargs['keys'])
            self.values = self._validate_argument(kwargs['values'])
        else:
            of = kwargs['of']
            if isinstance(of, tuple):
                try:
                    self.keys, self.values = map(self._validate_argument, of)
                except ValueError:
                    raise TypeError(
                        'of= tuple has to be a pair of matchers/types' % (
                        self.__class__.__name__,))
            else:
                self.items = self._validate_argument(of)