def _normalize(self, string):
    string = string.replace('\xa0', '')
    string = string.strip()
    return string