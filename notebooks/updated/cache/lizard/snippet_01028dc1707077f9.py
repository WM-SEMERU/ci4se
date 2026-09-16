def create_dampening(self, trigger_id, dampening):
    data = self._serialize_object(dampening)
    url = self._service_url(['triggers', trigger_id, 'dampenings'])
    return Dampening(self._post(url, data))