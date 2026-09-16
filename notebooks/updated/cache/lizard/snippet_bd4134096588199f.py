def add(self, option):
    if option.__class__ == Option:
        for _option in self.options:
            if option.name == _option.name:
                raise OptionDuplicateError(_option.name)
        self.options.append(option)
    else:
        raise TypeError('invalid type supplied')