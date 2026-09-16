def classificationgroup(self):
    path = ['author-profile', 'classificationgroup', 'classifications',
        'classification']
    out = [(item['$'], item['@frequency']) for item in listify(chained_get(
        self._json, path, []))]
    return out or None