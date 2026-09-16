def pretty_arg_types(self):
    if self.is_method:
        types = self.get_arg_type_descriptors()
        return (_pretty_type(t) for t in types)
    else:
        return tuple()