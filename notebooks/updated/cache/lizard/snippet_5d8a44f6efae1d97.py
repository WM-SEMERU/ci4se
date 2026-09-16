def trainTopicGetTrainedTopic(self, uri, maxConcepts=20, maxCategories=10,
    ignoreConceptTypes=[], idfNormalization=True):
    return self._er.jsonRequestAnalytics('/api/v1/trainTopic', {'action':
        'getTrainedTopic', 'uri': uri, 'maxConcepts': maxConcepts,
        'maxCategories': maxCategories, 'idfNormalization': idfNormalization})