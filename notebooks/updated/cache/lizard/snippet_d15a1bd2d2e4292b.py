def to_json(self):
    data = dict()
    data['name'] = self.name
    data['language'] = self.language
    data['fancy_name'] = self.fancy_name
    data['scenario'] = self.scenario
    return data