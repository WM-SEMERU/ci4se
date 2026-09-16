def make_descriptors(self, base_name):
    units_name = base_name + '_units'
    units_props = self._units_type.make_descriptors(units_name)
    return units_props + [UnitsSpecPropertyDescriptor(base_name, self,
        units_props[0])]