def parents_from_boolRule(self, rule):
    rule_pa = rule.replace('(', '').replace(')', '').replace('or', '').replace(
        'and', '').replace('not', '')
    rule_pa = rule_pa.split()
    if not rule_pa:
        return []
    pa_old = []
    pa_delete = []
    for pa in rule_pa:
        if pa not in self.varNames.keys():
            settings.m(0, 'list of available variables:')
            settings.m(0, list(self.varNames.keys()))
            message = ('processing of rule "' + rule +
                ' yields an invalid parent: ' + pa +
                """ | check whether the syntax is correct: 
""" +
                'only python expressions "(",")","or","and","not" ' +
                'are allowed, variable names and expressions have to be separated '
                 + 'by white spaces')
            raise ValueError(message)
        if pa in pa_old:
            pa_delete.append(pa)
    for pa in pa_delete:
        rule_pa.remove(pa)
    return rule_pa