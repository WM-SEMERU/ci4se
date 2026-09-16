def get_all_parcels(self, view=None):
    return parcels.get_all_parcels(self._get_resource_root(), self.name, view)