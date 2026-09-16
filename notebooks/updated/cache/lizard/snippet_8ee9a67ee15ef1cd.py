def add_child_resource_client(self, res_name, res_spec):
    res_spec = dict(res_spec)
    res_spec['name'] = res_name
    res = self.client_resource_factory(res_spec, parent=self, logger=self.
        _logger)
    self.children[resource.escape_name(res_name)] = res
    self._children_dirty = True
    res.set_ioloop(self.ioloop)
    res.start()
    return res