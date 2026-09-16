def get_parameter(self, path, default=None, return_group=False):
    value = read_parameter_by_path(self.job['config']['parameters'], path,
        return_group)
    if value is None:
        return default
    return value