def update(self):
    self.rules_map = {}
    self.skippable_rules = []
    for rule in self.rules:
        if not isinstance(rule, Rule):
            raise TypeError('item must be Rule instance', type(rule))
        self.rules_map.setdefault(rule.name, []).append(rule)
        if rule.skip:
            self.skippable_rules.append(rule)