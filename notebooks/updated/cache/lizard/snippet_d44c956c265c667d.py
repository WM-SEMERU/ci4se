def wrap(self, value):
    return self._parent.new_query().get_query().get_grammar().wrap(value)