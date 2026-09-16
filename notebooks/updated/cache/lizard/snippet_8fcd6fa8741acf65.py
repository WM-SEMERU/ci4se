def find(self, name):
    for i, nm in enumerate(self.data):
        if nm[-1] == name:
            return i
    return -1