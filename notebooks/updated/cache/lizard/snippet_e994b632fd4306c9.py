def requires(condition):

    def _decorator(func, condition=condition):
        if U.has_fun_prop(func, 'requires'):
            if not isinstance(U.get_fun_prop(func, 'requires'), list):
                raise E.InternalError('Invalid requires structure')
            base_requires = U.get_fun_prop(func, 'requires')
        else:
            base_requires = []
        base_condition = condition
        if '<-->' in condition:
            condition_parts = condition.split('<-->')
            assert len(condition_parts
                ) == 2, 'Only one implies per statement in %s condition %s' % (
                condition, func.__qualname__)
            condition = (
                '((%s) if (%s) else True) and ((%s) if (%s) else True)' % (
                condition_parts[1], condition_parts[0], condition_parts[0],
                condition_parts[1]))
        elif '-->' in condition:
            condition_parts = condition.split('-->')
            assert len(condition_parts
                ) == 2, 'Only one implies per statement in %s condition %s' % (
                base_condition, func.__qualname__)
            condition = '(%s) if (%s) else True' % (condition_parts[1],
                condition_parts[0])
        U.set_fun_prop(func, 'requires', [(compile(condition, '', 'eval'),
            condition)] + base_requires)
        return _wrap(func)
    return _decorator