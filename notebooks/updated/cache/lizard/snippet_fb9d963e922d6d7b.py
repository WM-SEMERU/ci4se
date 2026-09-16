def resolve(self):
    if self.source:
        result = self.source[1][self.source[0]]
        if result:
            return result
    return self.default