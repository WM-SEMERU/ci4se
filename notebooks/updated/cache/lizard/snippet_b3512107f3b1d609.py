def addStepListener(listener):
    if issubclass(type(listener), StepListener):
        _stepListeners.append(listener)
        return True
    warnings.warn(
        "Proposed listener's type must inherit from traci.StepListener. Not adding object of type '%s'"
         % type(listener))
    return False