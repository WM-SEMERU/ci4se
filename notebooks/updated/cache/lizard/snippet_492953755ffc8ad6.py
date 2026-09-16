def add_time_dependent_effects(self, ts):
    destts = Vectors.dense([0] * len(ts))
    result = self._jmodel.addTimeDependentEffects(_py2java(self._ctx,
        Vectors.dense(ts)), _py2java(self._ctx, destts))
    return _java2py(self._ctx, result.toArray())