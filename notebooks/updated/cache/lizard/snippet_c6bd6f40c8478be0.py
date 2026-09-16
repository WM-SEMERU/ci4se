def Name(self):
    name = ''
    if self.Version:
        name = self.Version.UserAgent
    return name