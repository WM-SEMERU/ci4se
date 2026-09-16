def remove_time_dependent_effects(self, ts):
    destts = Vectors.dense(np.array([0] * len(ts)))
    result = self._jmodel.removeTimeDependentEffects(_py2java(self._ctx,
        Vectors.dense(ts)), _py2java(self._ctx, destts))
    return _java2py(self._ctx, result.toArray())