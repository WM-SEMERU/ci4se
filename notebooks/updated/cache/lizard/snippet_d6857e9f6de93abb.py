def compute_tasks(self, **kwargs):
    params = self._prebuild(**kwargs)
    if not params:
        params = dict(kwargs)
    return self._build_tasks(**params)