def compareBulk(self, retina_name, body):
    resourcePath = '/compare/bulk'
    method = 'POST'
    queryParams = {}
    headerParams = {'Accept': 'Application/json', 'Content-Type':
        'application/json'}
    postData = None
    queryParams['retina_name'] = retina_name
    postData = body
    response = self.apiClient._callAPI(resourcePath, method, queryParams,
        postData, headerParams)
    return [metric.Metric(**r) for r in response.json()]