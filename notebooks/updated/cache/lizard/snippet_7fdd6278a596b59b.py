def _check_time_fn(self, time_instance=False):
    if time_instance and not isinstance(self.time_fn, param.Time):
        raise AssertionError('%s requires a Time object' % self.__class__.
            __name__)
    if self.time_dependent:
        global_timefn = self.time_fn is param.Dynamic.time_fn
        if global_timefn and not param.Dynamic.time_dependent:
            raise AssertionError(
                'Cannot use Dynamic.time_fn as parameters are ignoring time.')