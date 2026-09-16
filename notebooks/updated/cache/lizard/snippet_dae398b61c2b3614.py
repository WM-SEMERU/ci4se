def getReviews(self, setID):
    params = {'apiKey': self.apiKey, 'setID': setID}
    url = Client.ENDPOINT.format('getReviews')
    returned = get(url, params=params)
    self.checkResponse(returned)
    root = ET.fromstring(returned.text)
    return [Review(i) for i in root]