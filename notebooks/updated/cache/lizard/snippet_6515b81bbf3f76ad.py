def to_json(self):
    if self.indicator_variable is None:
        indicator = None
    else:
        indicator = self.indicator_variable.name
    json_obj = {'name': self.name, 'expression': expr_to_json(self.
        expression), 'lb': self.lb, 'ub': self.ub, 'indicator_variable':
        indicator, 'active_when': self.active_when}
    return json_obj