def DEFINE_bool(self, name, default, help, constant=False):
    self.AddOption(type_info.Bool(name=name, default=default, description=
        help), constant=constant)