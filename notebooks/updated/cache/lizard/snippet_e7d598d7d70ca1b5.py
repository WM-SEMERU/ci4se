def show_subnetpool(self, subnetpool, **_params):
    return self.get(self.subnetpool_path % subnetpool, params=_params)