def _bprop_wrap(name, reqtype, doc):

    def fget(self):
        return self._subqueries.get(name)

    def fset(self, value):
        if value is None:
            if name in self._subqueries:
                del self._subqueries[name]
        elif isinstance(value, reqtype):
            self._subqueries[name] = value
        elif isinstance(value, Query):
            self._subqueries[name] = reqtype(value)
        else:
            try:
                it = iter(value)
            except ValueError:
                raise TypeError('Value must be instance of Query')
            l = []
            for q in it:
                if not isinstance(q, Query):
                    raise TypeError('Item is not a query!', q)
                l.append(q)
            self._subqueries[name] = reqtype(*l)

    def fdel(self):
        setattr(self, name, None)
    return property(fget, fset, fdel, doc)