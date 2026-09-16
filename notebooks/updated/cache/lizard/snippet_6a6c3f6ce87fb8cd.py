def save_dataset(self, dataset, filename=None, fill_value=None, compute=
    True, **kwargs):
    raise NotImplementedError(
        "Writer '%s' has not implemented dataset saving" % (self.name,))