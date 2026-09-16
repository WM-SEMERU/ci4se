def enableBranch(self, enabled):
    self.enabled = enabled
    enabled = enabled and self.data != self.childrenDisabledValue
    for child in self.childItems:
        child.enableBranch(enabled)