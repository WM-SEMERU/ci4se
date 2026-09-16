def _validate_isvalid_unit(self, isvalid_unit, field, value):
    quantity = 1.0 * units(value['units'])
    try:
        quantity.to(property_units[field])
    except pint.DimensionalityError:
        self._error(field, 'incompatible units; should be consistent with ' +
            property_units[field])