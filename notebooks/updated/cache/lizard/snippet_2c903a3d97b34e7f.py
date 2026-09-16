def get_merged_params(self, supplied_params=None):
    supplied_params = supplied_params or {}
    empty_params = {param: supplied_params[param] for param in
        supplied_params if supplied_params[param] in (None, '')}
    if empty_params:
        warnings.warn(
            'The {path} endpoint was called with empty parameters: {empty_params}'
            .format(path=self.path, empty_params=empty_params),
            RuntimeWarning, stacklevel=5)
    unfulfilled_params = {param for param in self.required_params if param
         not in supplied_params and param not in self.default_params}
    if unfulfilled_params:
        raise UnfulfilledParameterException(self.path, unfulfilled_params)
    merged_params = self.default_params.copy()
    merged_params.update(supplied_params)
    return merged_params