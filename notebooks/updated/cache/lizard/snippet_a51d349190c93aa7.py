def subscribe(self, _func=None, needs=(), returns=(), modifies=(), **conditions
    ):
    modifies = set(modifies)
    parameters = set(needs) | modifies
    needs = parameters | set(conditions)
    if not needs:
        raise ValueError('tried to hook nothing')
    returns = set(returns) | modifies

    def deco(func):
        self.hooks.append(_Hook(func, needs, parameters, returns, conditions))
        return func
    if _func is not None:
        deco(_func)
    else:
        return deco