def sendStatusPing(self):
    data = parse.urlencode({'key': self.key, 'version': self.version}).encode()
    req = request.Request('https://redunda.sobotics.org/status.json', data)
    response = request.urlopen(req)
    jsonReturned = json.loads(response.read().decode('utf-8'))
    self.location = jsonReturned['location']
    self.shouldStandby = jsonReturned['should_standby']
    self.eventCount = jsonReturned['event_count']