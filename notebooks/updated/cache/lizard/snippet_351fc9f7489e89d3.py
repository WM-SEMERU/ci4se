def request_single(self, name, content={}):
    resp = self.request(name, content)
    for i in resp.values():
        if type(i) == list:
            return i[0]
        elif type(i) == dict:
            return i
    return None