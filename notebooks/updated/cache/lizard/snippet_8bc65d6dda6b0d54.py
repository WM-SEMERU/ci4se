def get_spaces(self):
    self.spaces = []
    for resource in self._get_spaces()['resources']:
        self.spaces.append(resource['entity']['name'])
    return self.spaces