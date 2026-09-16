def getEnable(self, name, default=False, parent_search=False,
    multikeys_search=False):
    value = self.get(name, default, parent_search, multikeys_search)
    if type(value) != str:
        return value == 1 or value
    return value.lower() in ['true', 't', '1', 'oui', 'vrai', 'v', 'on',
        'o', 'yes', 'y', 'si', 's', 'da', 'd', 'ja', 'j']