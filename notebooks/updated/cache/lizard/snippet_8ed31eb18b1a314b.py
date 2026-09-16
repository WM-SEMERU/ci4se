def as_dict(self):
    opt_info = {}
    opt_info['type'] = 'value'
    opt_info['name'] = self.name
    opt_info['value'] = self.value
    opt_info['otype'] = self.otype.as_dict()
    return opt_info