def check_fill_value_outside_valid_range(self, ds):
    valid_fill_range = TestCtx(BaseCheck.MEDIUM, self.section_titles['2.5'])
    for name, variable in ds.variables.items():
        if not hasattr(variable, '_FillValue'):
            continue
        fill_value = variable._FillValue
        attrs = variable.ncattrs()
        if 'valid_range' in attrs:
            if isinstance(variable.valid_range, basestring):
                m = (
                    '§2.5.1 Fill Values should be outside the range specified by valid_range'
                    )
                valid_fill_range.assert_true(False,
                    """{};
	{}:valid_range must be a numeric type not a string"""
                    .format(m, name))
                continue
            rmin, rmax = variable.valid_range
            spec_by = 'valid_range'
        elif 'valid_min' in attrs and 'valid_max' in attrs:
            if isinstance(variable.valid_min, basestring):
                valid_fill_range.assert_true(False,
                    '{}:valid_min must be a numeric type not a string'.
                    format(name))
            if isinstance(variable.valid_max, basestring):
                valid_fill_range.assert_true(False,
                    '{}:valid_max must be a numeric type not a string'.
                    format(name))
            if isinstance(variable.valid_min, basestring) or isinstance(
                variable.valid_max, basestring):
                continue
            rmin = variable.valid_min
            rmax = variable.valid_max
            spec_by = 'valid_min/valid_max'
        else:
            continue
        if np.isnan(fill_value):
            valid = True
        else:
            valid = fill_value < rmin or fill_value > rmax
        valid_fill_range.assert_true(valid,
            '{}:_FillValue ({}) should be outside the range specified by {} ({}, {})'
            .format(name, fill_value, spec_by, rmin, rmax))
    return valid_fill_range.to_result()