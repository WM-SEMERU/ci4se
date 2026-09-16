def init_resource(self, request, res):
    res.location_query = request.uri_query
    res.payload = request.content_type, request.payload
    return res