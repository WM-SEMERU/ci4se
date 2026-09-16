def get_extensions(self, support=None):
    return [x for x in self.extensions.values() if support and support in x
        .supported or not support]