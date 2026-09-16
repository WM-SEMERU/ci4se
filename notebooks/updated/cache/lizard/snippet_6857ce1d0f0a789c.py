def create_set(self, set_id, etype, entities):
    if etype not in {'sample', 'pair', 'participant'}:
        raise ValueError('Unsupported entity type:' + str(etype))
    payload = 'membership:' + etype + '_set_id\t' + etype + '_id\n'
    for e in entities:
        if e.etype != etype:
            msg = "Entity type '" + e.etype + "' does not match "
            msg += "set type '" + etype + "'"
            raise ValueError(msg)
        payload += set_id + '\t' + e.entity_id + '\n'
    r = fapi.upload_entities(self.namespace, self.name, payload, self.api_url)
    fapi._check_response_code(r, 201)