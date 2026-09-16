def match(self, passageId):
    if not isinstance(passageId, CtsReference):
        passageId = CtsReference(passageId)
    if self.is_root():
        return self[passageId.depth - 1]
    return self.root.match(passageId)