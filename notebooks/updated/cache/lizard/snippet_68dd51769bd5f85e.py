def get_list_endpoint(self, rel='instances'):
    schema_loaded = not self.schema is None
    links_present = 'links' in self.schema.keys()
    if schema_loaded and links_present:
        for row in self.schema['links']:
            if row['rel'] == rel:
                return row
    raise APIException('ENDPOINT_NOTFOUND', 'invalid endpoint')