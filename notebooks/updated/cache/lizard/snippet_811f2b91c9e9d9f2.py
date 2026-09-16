def apply(self, func, applyto='measurement', noneval=nan, setdata=False):
    applyto = applyto.lower()
    if applyto == 'data':
        if self.data is not None:
            data = self.data
        elif self.datafile is None:
            return noneval
        else:
            data = self.read_data()
            if setdata:
                self.data = data
        return func(data)
    elif applyto == 'measurement':
        return func(self)
    else:
        raise ValueError(
            'Encountered unsupported value "%s" for applyto parameter.' %
            applyto)