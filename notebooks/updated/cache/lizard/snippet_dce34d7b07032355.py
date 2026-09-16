def _to_dict(self):
    physical_prop_names = find_PhysicalProperty(self)
    physical_prop_vals = [getattr(self, prop) for prop in physical_prop_names]
    return dict(zip(physical_prop_names, physical_prop_vals))