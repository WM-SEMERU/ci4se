def startMultiple(self, zones):
    path = 'zone/start_multiple'
    payload = {'zones': zones}
    return self.rachio.put(path, payload)