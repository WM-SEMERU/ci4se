def getProperty(self, orgresource, dummy=56184):
    url = nurls['getProperty']
    data = {'userid': self.user_id, 'useridx': self.useridx, 'dummy': dummy,
        'orgresource': orgresource}
    r = self.session.post(url=url, data=data)
    j = json.loads(r.text)
    if self.resultManager(r.text):
        f = FileInfo()
        result = j['resultvalue']
        f.resourcetype = result['resourcetype']
        f.resourceno = result['resourceno']
        return f
    else:
        return False