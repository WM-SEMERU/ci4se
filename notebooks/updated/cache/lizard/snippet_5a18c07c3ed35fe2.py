def addLocation(self, locationUri, weight):
    assert isinstance(weight, (float, int)
        ), 'weight value has to be a positive or negative integer'
    self.topicPage['locations'].append({'uri': locationUri, 'wgt': weight})