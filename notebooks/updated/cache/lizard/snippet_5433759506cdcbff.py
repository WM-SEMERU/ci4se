def add_single(self, address, rank=1, nodeid=1, ospf_area=None, **kwargs):
    lb = self.create(address, rank, nodeid, ospf_area, **kwargs)
    self._engine.nodes[0].data[self.typeof].append(lb.data)
    self._engine.update()