def create_field(self, collection, field_dict):
    if self.does_field_exist(collection, field_dict['name']):
        raise ValueError('Field {} Already Exists in Solr Collection {}'.
            format(field_dict['name'], collection))
    temp = {'add-field': dict(field_dict)}
    res, con_info = self.solr.transport.send_request(method='POST',
        endpoint=self.schema_endpoint, collection=collection, data=json.
        dumps(temp))
    return res