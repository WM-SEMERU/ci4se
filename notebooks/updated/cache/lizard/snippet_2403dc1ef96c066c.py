def get_resources(self, types=None, names=None, languages=None):
    return GetResources(self.filename, types, names, languages)