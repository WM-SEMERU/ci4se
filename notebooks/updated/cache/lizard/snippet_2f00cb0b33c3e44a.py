def purgeAutoSelected(self):
    params = self._autoParams.allData()
    for p in params:
        comps_to_remove = []
        for comp in p['selection']:
            if self.indexByComponent(comp) is None:
                comps_to_remove.append(comp)
        for orphaned in comps_to_remove:
            p['selection'].remove(orphaned)