def flip_constraint(self, twig=None, solve_for=None, **kwargs):
    self._kwargs_checks(kwargs, additional_allowed_keys=['check_nan'])
    kwargs['twig'] = twig
    redo_kwargs = deepcopy(kwargs)
    undo_kwargs = deepcopy(kwargs)
    changed_params = self.run_delayed_constraints()
    param = self.get_constraint(**kwargs)
    if kwargs.pop('check_nan', True) and np.any(np.isnan([p.get_value() for
        p in param.vars.to_list()])):
        raise ValueError('cannot flip constraint while the value of {} is nan'
            .format([p.twig for p in param.vars.to_list() if np.isnan(p.
            get_value())]))
    if solve_for is None:
        return param
    if isinstance(solve_for, Parameter):
        solve_for = solve_for.uniquetwig
    redo_kwargs['solve_for'] = solve_for
    undo_kwargs['solve_for'] = param.constrained_parameter.uniquetwig
    logger.info("flipping constraint '{}' to solve for '{}'".format(param.
        uniquetwig, solve_for))
    param.flip_for(solve_for)
    result = self.run_constraint(uniqueid=param.uniqueid,
        skip_kwargs_checks=True)
    self._add_history(redo_func='flip_constraint', redo_kwargs=redo_kwargs,
        undo_func='flip_constraint', undo_kwargs=undo_kwargs)
    return param