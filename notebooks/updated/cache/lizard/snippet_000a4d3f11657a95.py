def guard_activate(analysis_service):
    calculation = analysis_service.getCalculation()
    if not calculation:
        return True
    if not api.is_active(calculation):
        return False
    dependencies = calculation.getDependentServices()
    for dependency in dependencies:
        if not api.is_active(dependency):
            return False
    return True