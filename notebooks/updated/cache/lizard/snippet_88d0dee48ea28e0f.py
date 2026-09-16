def recalculate(self, parent, updates):
    rule_function, children = self._aggregates[parent]
    rule_function(parent, children)