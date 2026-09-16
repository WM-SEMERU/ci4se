def attr_exists(self, attr):
    gen = self.attr_gen(attr)
    n_instances = len(list(gen))
    if n_instances > 0:
        return True
    else:
        return False