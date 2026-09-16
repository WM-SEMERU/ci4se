def isAboveUpperDetectionLimit(self):
    if self.isUpperDetectionLimit():
        return True
    result = self.getResult()
    if result and str(result).strip().startswith(UDL):
        return True
    if api.is_floatable(result):
        return api.to_float(result) > self.getUpperDetectionLimit()
    return False