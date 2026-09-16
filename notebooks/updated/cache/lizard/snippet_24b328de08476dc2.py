def set_rules(self, rules):
    options = {}
    if rules:
        if rules.get('ignore'):
            options['rules'] = {}
            for rule in rules.get('ignore'):
                options['rules'][rule] = {'enabled': False}
        elif rules.get('apply'):
            options['runOnly'] = {'type': 'rule', 'values': rules.get('apply')}
        elif rules.get('tags'):
            options['runOnly'] = {'type': 'tag', 'values': rules.get('tags')}
    self.rules = json.dumps(options)