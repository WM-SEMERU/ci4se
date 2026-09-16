def mask(self):
    if self.filter_func is None:
        raise RuntimeError("Can't get a mask without a filter function!")
    else:
        if self._mask is None:
            for column in self.columns:
                if column in self.filter_func:
                    setattr(self, column, self.group[column][:])
            self._mask = eval(self.filter_func)
        return self._mask