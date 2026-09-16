def send_to_contact(self, obj_id, contact_id):
    response = self._client.session.post('{url}/{id}/send/contact/{contact_id}'
        .format(url=self.endpoint_url, id=obj_id, contact_id=contact_id))
    return self.process_response(response)