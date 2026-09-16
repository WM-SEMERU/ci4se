def add_item(self, collection_uri, name, metadata):
    metadata['dcterms:identifier'] = name
    metadata['dc:identifier'] = name
    metadata['@type'] = 'ausnc:AusNCObject'
    meta = {'items': [{'metadata': {'@context': self.context, '@graph': [
        metadata]}}]}
    response = self.api_request(collection_uri, method='POST', data=json.
        dumps(meta))
    self.__check_success(response)
    item_uri = collection_uri + '/' + response['success'][0]
    return item_uri