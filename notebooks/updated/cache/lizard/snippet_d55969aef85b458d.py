def check_dimensionless_vertical_coordinate(self, ds):
    ret_val = []
    z_variables = cfutil.get_z_variables(ds)
    deprecated_units = ['level', 'layer', 'sigma_level']
    for name in z_variables:
        variable = ds.variables[name]
        standard_name = getattr(variable, 'standard_name', None)
        units = getattr(variable, 'units', None)
        formula_terms = getattr(variable, 'formula_terms', None)
        if (formula_terms is None and standard_name not in
            dimless_vertical_coordinates):
            continue
        is_not_deprecated = TestCtx(BaseCheck.LOW, self.section_titles['4.3'])
        is_not_deprecated.assert_true(units not in deprecated_units,
            '§4.3.2: units are deprecated by CF in variable {}: {}'.format(
            name, units))
        ret_val.append(is_not_deprecated.to_result())
        ret_val.append(self._check_formula_terms(ds, name))
    return ret_val