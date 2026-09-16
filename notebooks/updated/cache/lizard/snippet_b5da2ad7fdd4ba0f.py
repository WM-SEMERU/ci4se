def delete(self, data_src):
    items = self.objects[data_src].data.keys()
    self.reg.unregister(items)
    self.layer.pop(data_src)
    self.objects.pop(data_src)
    self.sources.pop(data_src)