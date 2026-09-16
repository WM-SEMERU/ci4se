def _inventory(self):
    if self.dynamic_version_of:
        return self.dynamic_version_of._inventory
    if not hasattr(self, '_inventory_field'):
        self._inventory_field = limpyd_fields.SetField()
        self._inventory_field._attach_to_model(self._model)
        self._inventory_field._attach_to_instance(self._instance)
        self._inventory_field.lockable = True
        self._inventory.name = self.name
    return self._inventory_field