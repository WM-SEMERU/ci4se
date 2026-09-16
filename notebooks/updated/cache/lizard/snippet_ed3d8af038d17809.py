def _check_formula_terms(self, ds, coord):
    variable = ds.variables[coord]
    standard_name = getattr(variable, 'standard_name', None)
    formula_terms = getattr(variable, 'formula_terms', None)
    valid_formula_terms = TestCtx(BaseCheck.HIGH, self.section_titles['4.3'])
    valid_formula_terms.assert_true(isinstance(formula_terms, basestring) and
        formula_terms,
        "§4.3.2: {}'s formula_terms is a required attribute and must be a non-empty string"
        .format(coord))
    if not formula_terms:
        return valid_formula_terms.to_result()
    matches = regex.findall('([A-Za-z][A-Za-z0-9_]*: )([A-Za-z][A-Za-z0-9_]*)',
        variable.formula_terms)
    terms = set(m[0][:-2] for m in matches)
    missing_vars = sorted(set(m[1] for m in matches) - set(ds.variables))
    missing_fmt = (
        'The following variable(s) referenced in {}:formula_terms are not present in the dataset: {}'
        )
    valid_formula_terms.assert_true(len(missing_vars) == 0, missing_fmt.
        format(coord, ', '.join(missing_vars)))
    reconstructed_formula = ' '.join(m[0] + m[1] for m in matches)
    valid_formula_terms.assert_true(reconstructed_formula == formula_terms,
        'Attribute formula_terms is not well-formed')
    valid_formula_terms.assert_true(standard_name in
        dimless_vertical_coordinates,
        "unknown standard_name '{}' for dimensionless vertical coordinate {}"
        .format(standard_name, coord))
    if standard_name not in dimless_vertical_coordinates:
        return valid_formula_terms.to_result()
    valid_formula_terms.assert_true(no_missing_terms(standard_name, terms),
        "{}'s formula_terms are invalid for {}, please see appendix D of CF 1.6"
        .format(coord, standard_name))
    return valid_formula_terms.to_result()