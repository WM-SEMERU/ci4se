def _add_choice_getter(self):
    property_ = property(self._choice_getter, None, None)
    setattr(self._element_cls, self._prop_name, property_)