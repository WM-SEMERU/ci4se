def get_units_property(self, *, unit_ids=None, property_name):
    if unit_ids is None:
        unit_ids = self.get_unit_ids()
    values = [self.get_unit_property(unit_id=unit, property_name=
        property_name) for unit in unit_ids]
    return values