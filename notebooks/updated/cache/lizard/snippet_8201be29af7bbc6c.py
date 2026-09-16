def _check_flag_values(self, ds, name):
    variable = ds.variables[name]
    flag_values = variable.flag_values
    flag_meanings = getattr(variable, 'flag_meanings', None)
    valid_values = TestCtx(BaseCheck.HIGH, self.section_titles['3.5'])
    valid_values.assert_true(isinstance(flag_values, np.ndarray),
        "{}'s flag_values must be an array of values not {}".format(name,
        type(flag_values)))
    if not isinstance(flag_values, np.ndarray):
        return valid_values.to_result()
    flag_set = set(flag_values)
    valid_values.assert_true(len(flag_set) == len(flag_values),
        "{}'s flag_values must be independent and can not be repeated".
        format(name))
    valid_values.assert_true(variable.dtype.type == flag_values.dtype.type,
        'flag_values ({}) must be the same data type as {} ({})'.format(
        flag_values.dtype.type, name, variable.dtype.type))
    if isinstance(flag_meanings, basestring):
        flag_meanings = flag_meanings.split()
        valid_values.assert_true(len(flag_meanings) == len(flag_values), 
            "{}'s flag_meanings and flag_values should have the same number "
            .format(name) + 'of elements.')
    return valid_values.to_result()