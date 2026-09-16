def diff_array(self, features, force=True, func=None, array_kwargs=dict(),
    cache=None):
    self.features = list(features)
    self.browser_local_coverage_kwargs = array_kwargs.copy()
    self.browser_local_coverage_kwargs.pop('processes', None)
    self.browser_local_coverage_kwargs.pop('chunksize', 1)
    self.array_kwargs = array_kwargs.copy()
    if self.ip_array is None or force:
        self.ip_array = self.ip.array(features, **array_kwargs)
        self.ip_array /= self.ip.mapped_read_count() / 1000000.0
    if self.control_array is None or force:
        self.control_array = self.control.array(features, **array_kwargs)
        self.control_array /= self.control.mapped_read_count() / 1000000.0
    if func is None:
        self.diffed_array = self.ip_array - self.control_array
    else:
        self.diffed_array = func(self.ip_array - self.control_array)