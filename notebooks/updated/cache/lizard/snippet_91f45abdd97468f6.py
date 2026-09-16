def _decode_request(self, encoded_request):
    obj = self.serializer.loads(encoded_request)
    return request_from_dict(obj, self.spider)