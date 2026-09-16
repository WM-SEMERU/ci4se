def fit(self, y, exogenous=None, **fit_kwargs):
    steps = self.steps_ = self._validate_steps()
    yt = y
    Xt = exogenous
    named_kwargs = self._get_kwargs(**fit_kwargs)
    for step_idx, name, transformer in self._iter(with_final=False):
        cloned_transformer = clone(transformer)
        kwargs = named_kwargs[name]
        yt, Xt = cloned_transformer.fit_transform(yt, Xt, **kwargs)
        steps[step_idx] = name, cloned_transformer
    kwargs = named_kwargs[steps[-1][0]]
    self._final_estimator.fit(yt, exogenous=Xt, **kwargs)
    return self