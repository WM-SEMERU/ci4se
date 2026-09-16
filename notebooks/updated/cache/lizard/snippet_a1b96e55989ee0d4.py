def get_args(self, client):
    default_args = self.default_args(client)
    if self.method_args or self.optional_args:
        optional_args = getattr(self, 'optional_args', tuple())
        args = []
        for arg in (self.method_args + optional_args):
            if hasattr(self, arg):
                obj = getattr(self, arg)
                if hasattr(obj, 'struct'):
                    args.append(obj.struct)
                else:
                    args.append(obj)
        args = list(default_args) + args
    else:
        args = default_args
    return args