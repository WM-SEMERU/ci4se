def name_with_version(self):
    if self.version == 1:
        return self.name
    else:
        return '{}:{}'.format(self.name, self.version)