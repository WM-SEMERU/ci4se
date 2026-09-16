def default_parse(self, string):
    results = list()
    while string:
        token = self.longest(string)
        results.append(token)
        string = string[len(token):]
    return results