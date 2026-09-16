def check(self, value, namespace):
    return namespace.is_compatible(self.typevar, type(value))