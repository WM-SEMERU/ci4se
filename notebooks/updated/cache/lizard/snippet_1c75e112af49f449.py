def manipulate(self, stored_instance, component_instance):
    self._ipopo_instance = stored_instance
    self._context = stored_instance.bundle_context
    setattr(component_instance, self._field, {})