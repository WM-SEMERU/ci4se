def _isCompatible(self, other, reporter):
    component1 = self
    component2 = other
    if component1.baseName != component2.baseName:
        reporter.baseDifference = True
        reporter.warning = True