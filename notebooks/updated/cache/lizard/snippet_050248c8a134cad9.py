def getAnalyst(self):
    analyst = self.getField('Analyst').get(self)
    if not analyst:
        analyst = self.getSubmittedBy()
    return analyst or ''