def resource(self):
    if self._resource:
        return self._resource
    elif self.binding:
        return self.binding.resource