def get_configuration_set_by_id(self, id):
    for cs in self.configuration_sets:
        if cs.id == id:
            return cs
    return None