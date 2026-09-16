def getDelOps(self, buid):
    return ('prop:del', (buid, self.form.name, self.name, self.storinfo)),