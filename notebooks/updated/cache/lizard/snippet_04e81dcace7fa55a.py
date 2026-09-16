def _serialize_object(self, response_data, request):
    if not self.factory:
        return response_data
    if isinstance(response_data, (list, tuple)):
        return map(lambda item: self.factory.serialize(item, request),
            response_data)
    else:
        return self.factory.serialize(response_data, request)