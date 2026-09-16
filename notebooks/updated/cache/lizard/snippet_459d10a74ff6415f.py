def evaluate(self, environment=None):
    current_environment = default_environment()
    if environment is not None:
        current_environment.update(environment)
    return _evaluate_markers(self._markers, current_environment)