def is_uncertainty_edition_allowed(self, analysis_brain):
    if not self.is_result_edition_allowed(analysis_brain):
        return False
    obj = api.get_object(analysis_brain)
    if not obj.getAllowManualUncertainty():
        return False
    if obj.getDetectionLimitOperand() in [LDL, UDL]:
        return False
    return True