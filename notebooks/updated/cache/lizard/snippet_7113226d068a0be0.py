def load(self):
    variables = FrozenOrderedDict((_decode_variable_name(k), v) for k, v in
        self.get_variables().items())
    attributes = FrozenOrderedDict(self.get_attrs())
    return variables, attributes