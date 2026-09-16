def add_field(self, name, default=None, required=False, error=None):
    if name is None:
        return
    self.field_arguments.append(dict(name=name, default=default, required=
        required, error=error))