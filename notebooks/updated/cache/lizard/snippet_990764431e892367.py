def scaleField(self, scalingFactor):
    oldField = self.fieldReduction.val
    newField = 100.0 * (scalingFactor * (1.0 + oldField / 100.0) - 1.0)
    self.fieldReduction = self.fieldReduction._replace(val=newField)