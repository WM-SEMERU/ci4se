def registerParentFlag(self, optionName, value):
    self.parentFlags.update({optionName: value})
    return self