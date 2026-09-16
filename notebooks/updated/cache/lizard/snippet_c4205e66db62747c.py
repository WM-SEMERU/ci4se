def links(self):
    dlinks = {}
    for key, value in self.__dict__.items():
        if isinstance(value, dict) and value['link']:
            dlinks[key] = value['link']
    return dlinks