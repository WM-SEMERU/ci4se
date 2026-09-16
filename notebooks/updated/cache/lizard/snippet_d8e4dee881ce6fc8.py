def add_filter_rule(self, name, condition, filters, actions, active=1, way='in'
    ):
    filters['condition'] = condition
    new_rule = {'name': name, 'active': active, 'filterTests': filters,
        'filterActions': actions}
    new_rules = [zobjects.FilterRule.from_dict(new_rule)]
    prev_rules = self.get_filter_rules(way=way)
    if prev_rules:
        for rule in prev_rules:
            if rule.name == new_rules[0].name:
                raise ZimSOAPException('filter %s already exists' % rule.name)
        new_rules = new_rules + prev_rules
    content = {'filterRules': {'filterRule': [r._full_data for r in new_rules]}
        }
    if way == 'in':
        self.request('ModifyFilterRules', content)
    elif way == 'out':
        self.request('ModifyOutgoingFilterRules', content)
    return new_rules