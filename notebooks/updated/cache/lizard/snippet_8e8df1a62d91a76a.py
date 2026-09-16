def withArgs(self, *args, **kwargs):
    cond_args = args if len(args) > 0 else None
    cond_kwargs = kwargs if len(kwargs) > 0 else None
    return _SinonStubCondition(copy=self._copy, cond_args=cond_args,
        cond_kwargs=cond_kwargs, oncall=self._oncall)