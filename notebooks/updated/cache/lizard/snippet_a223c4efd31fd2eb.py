def _map_intent_to_view_func(self, intent):
    if intent.name in self._intent_view_funcs:
        view_func = self._intent_view_funcs[intent.name]
    elif self._default_intent_view_func is not None:
        view_func = self._default_intent_view_func
    else:
        raise NotImplementedError(
            'Intent "{}" not found and no default intent specified.'.format
            (intent.name))
    PY3 = sys.version_info[0] == 3
    if PY3:
        argspec = inspect.getfullargspec(view_func)
    else:
        argspec = inspect.getargspec(view_func)
    arg_names = argspec.args
    arg_values = self._map_params_to_view_args(intent.name, arg_names)
    return partial(view_func, *arg_values)