def create(self):
    self.validate()
    body = soap_request.new_folder(self)
    response_xml = self.service.send(body)
    self._id, self._change_key = self._parse_id_and_change_key_from_response(
        response_xml)
    return self