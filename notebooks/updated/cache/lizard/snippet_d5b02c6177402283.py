def move_to(self, folder_id):
    if not folder_id:
        raise TypeError("You can't move an event to a non-existant folder")
    if not isinstance(folder_id, BASESTRING_TYPES):
        raise TypeError('folder_id must be a string')
    if not self.id:
        raise TypeError("You can't move an event that hasn't been created yet."
            )
    self.refresh_change_key()
    response_xml = self.service.send(soap_request.move_event(self, folder_id))
    new_id, new_change_key = self._parse_id_and_change_key_from_response(
        response_xml)
    if not new_id:
        raise ValueError(
            'MoveItem returned success but requested item not moved')
    self._id = new_id
    self._change_key = new_change_key
    self.calendar_id = folder_id
    return self