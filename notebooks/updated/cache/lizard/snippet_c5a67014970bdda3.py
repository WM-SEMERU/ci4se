def detect(self, source, description):
    if source == 'guid' and description in self.guids:
        return {self: 100}
    description = description.lower()
    if description == self.type:
        return {self: 100}
    elif re.search('\\b' + self.type + '\\b', description):
        return {self: 80}
    elif any(re.search('\\b' + alias + '\\b', description) for alias in
        self.aliases):
        return {self: 70}
    return {}