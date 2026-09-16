def get_embedded_object(self, signature_id):
    request = self._get_request()
    return request.get(self.EMBEDDED_OBJECT_GET_URL + signature_id)