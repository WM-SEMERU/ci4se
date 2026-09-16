def unit_transform(self, x, **kwargs):
    if len(kwargs) > 0:
        self.update(**kwargs)
    return self.distribution.ppf(x, *self.args, loc=self.loc, scale=self.scale)