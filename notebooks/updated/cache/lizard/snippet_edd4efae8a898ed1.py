def GetFingerprint(self, name):
    for result in self.results:
        if result.GetItem('name') == name:
            return result