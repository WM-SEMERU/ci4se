def del_option(self, option):
    assert isinstance(option, Option)
    while option in list(self._options):
        self._options.remove(option)