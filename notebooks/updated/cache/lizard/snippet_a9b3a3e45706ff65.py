def iterate_nodes(self, key, distinct=True):
    if not self.runtime._ring:
        yield None
    else:
        for node in self.range(key, unique=distinct):
            yield node['nodename']