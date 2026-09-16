def stem(self):
    base, ext = self.module.splitext(self.name)
    return base