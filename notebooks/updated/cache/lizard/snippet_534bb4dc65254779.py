def get(self, mail):
    users = (v for v in self.list() if v.get('mail') == mail)
    for i in users:
        self.log.debug(i)
        return i
    return None