def del_option_by_number(self, number):
    for o in list(self._options):
        assert isinstance(o, Option)
        if o.number == number:
            self._options.remove(o)