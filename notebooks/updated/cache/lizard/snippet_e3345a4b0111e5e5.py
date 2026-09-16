def delete_entity(self, etype, entity_id):
    r = fapi.delete_entity(self.namespace, self.name, etype, entity_id,
        self.api_url)
    fapi._check_response_code(r, 202)