def setup_data(self):
    data = self.data
    if len(data) == 0:
        return type(data)()
    data = self.geom.setup_data(data)
    check_required_aesthetics(self.geom.REQUIRED_AES, set(data.columns) |
        set(self.geom.aes_params), self.geom.__class__.__name__)
    self.data = data