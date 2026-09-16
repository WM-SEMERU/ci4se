def add_observer(self, observer, identify_observed=False):
    if hasattr(observer, '__self__'):
        result = self._add_bound_method(observer, identify_observed)
    else:
        result = self._add_function(observer, identify_observed)
    return result