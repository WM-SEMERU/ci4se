def move_to(self, folder_id):
    if not folder_id:
        raise TypeError("You can't move to a non-existant folder")
    if not isinstance(folder_id, BASESTRING_TYPES):
        raise TypeError('folder_id must be a string')
    if not self.id:
        raise TypeError("You can't move a folder that hasn't been created yet."
            )
    response_xml = self.service.send(soap_request.move_folder(self, folder_id))
    result_id, result_key = self._parse_id_and_change_key_from_response(
        response_xml)
    if self.id != result_id:
        raise ValueError(
            'MoveFolder returned success but requested folder not moved')
    self.parent_id = folder_id
    return self