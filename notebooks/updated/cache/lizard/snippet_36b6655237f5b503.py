def _get_init_args(self):
    args = {}
    for rop in self.ro_properties:
        if rop in self.properties:
            args[rop] = self.properties[rop]
    return args