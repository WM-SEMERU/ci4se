def add_rule(self, binding_type: str, rule: BindingRule):
    if binding_type not in self._rules:
        self._rules[binding_type] = []
    self._rules[binding_type].insert(0, rule)