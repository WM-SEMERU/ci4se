def doesNotContain(self, value):
    newq = self.copy()
    newq.setOp(Query.Op.DoesNotContain)
    newq.setValue(value)
    return newq