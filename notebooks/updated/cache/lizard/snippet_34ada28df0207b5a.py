def get(self, rule, default=None):
    assert isinstance(rule, ClassifierRule)
    if (rule.condition not in self._population or rule.action not in self.
        _population[rule.condition]):
        return default
    return self._population[rule.condition][rule.action]