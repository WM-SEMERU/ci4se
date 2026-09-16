def detach_all(self):
    self.detach_all_classes()
    self.objects.clear()
    self.index.clear()
    self._keepalive[:] = []