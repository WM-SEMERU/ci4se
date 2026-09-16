def greaterThanOrEqual(self, value):
    newq = self.copy()
    newq.setOp(Query.Op.GreaterThanOrEqual)
    newq.setValue(value)
    return newq