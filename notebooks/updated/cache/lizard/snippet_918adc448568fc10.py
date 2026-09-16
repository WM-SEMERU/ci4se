def getServiceDependencies(self):
    calc = self.getCalculation()
    if calc:
        return calc.getCalculationDependencies(flat=True)
    return []