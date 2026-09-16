def _validate_measure_count(self, times):
    if not self.min_measures <= times <= self.max_measures:
        raise ParameterValidationError(
            '{times} is not within the borders defined in the class'.format
            (times=times))