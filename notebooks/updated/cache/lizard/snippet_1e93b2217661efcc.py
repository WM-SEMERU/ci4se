def match(self, description):
    rules = []
    ordered_rules = []
    description = description.lower()
    for rule in self.extract_rules:
        if rule['regex'].search(description):
            rules.append(rule)
    for rule in rules:
        if callable(rule['cmd']):
            ordered_rules.append(rule)
    for rule in rules:
        if not callable(rule['cmd']):
            ordered_rules.append(rule)
    return ordered_rules