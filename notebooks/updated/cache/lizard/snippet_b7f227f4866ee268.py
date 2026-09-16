def _check_min_max_range(self, var, test_ctx):
    if 'valid_range' in var.ncattrs():
        test_ctx.assert_true(var.valid_range.dtype == var.dtype and len(var
            .valid_range) == 2 and var.valid_range[0] <= var.valid_range[1],
            'valid_range must be a two element vector of min followed by max with the same data type as {}'
            .format(var.name))
    else:
        for bound in ('valid_min', 'valid_max'):
            v_bound = getattr(var, bound, '')
            warn_msg = (
                '{} attribute should exist, have the same type as {}, and not be empty or valid_range should be defined'
                .format(bound, var.name))
            if isinstance(v_bound, six.string_types):
                test_ctx.assert_true(v_bound != '' and var.dtype.char ==
                    'S', warn_msg)
            else:
                test_ctx.assert_true(v_bound.dtype == var.dtype, warn_msg)
    return test_ctx