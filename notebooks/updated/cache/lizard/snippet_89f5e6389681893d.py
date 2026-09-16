def get_help_keys(self):
    help_keys = {}
    for k, v in self.help_context.items():
        if isinstance(v, tuple):
            help_keys[k] = v[0]
        else:
            help_keys[k] = v
    return help_keys