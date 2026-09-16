def get_public_methods(self):
    return self.get_action_methods() + [('getenv', self.getenv), (
        'expandvars', self.expandvars), ('defined', self.defined), (
        'undefined', self.undefined)]