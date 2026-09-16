def populate_class_members(self, element_cls, prop_name):
    super(ZeroOrOne, self).populate_class_members(element_cls, prop_name)
    self._add_getter()
    self._add_creator()
    self._add_inserter()
    self._add_adder()
    self._add_get_or_adder()
    self._add_remover()