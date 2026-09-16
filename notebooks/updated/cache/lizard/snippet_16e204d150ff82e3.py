def _update_job(self, target, args, kwargs):
    target_path, options = get_function_path_and_options(target)
    assert isinstance(args, (tuple, list)) or args is None
    assert isinstance(kwargs, dict) or kwargs is None
    if options:
        self.update_options(**options)
    self._options['job'] = target_path, args, kwargs