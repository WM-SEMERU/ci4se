def _delete_dynamic_versions(self):
    if self.dynamic_version_of:
        raise ImplementationError(
            '"_delete_dynamic_versions" can only be executed on the base field'
            )
    inventory = self._inventory
    for dynamic_part in inventory.smembers():
        name = self.get_name_for(dynamic_part)
        new_field = self._create_dynamic_version()
        new_field.name = name
        new_field._dynamic_part = dynamic_part
        new_field._attach_to_model(self._model)
        new_field._attach_to_instance(self._instance)
        new_field.delete()
    inventory.delete()