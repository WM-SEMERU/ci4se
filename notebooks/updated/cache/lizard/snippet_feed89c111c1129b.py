def main(self):
    for m in self.methods:
        if m.name in ['Main', 'main']:
            return m
    if len(self.methods):
        return self.methods[0]
    return None