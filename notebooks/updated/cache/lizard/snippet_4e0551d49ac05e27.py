def get_extended_metadata(self, item_id):
    response = self.soap_client.call('getExtendedMetadata', [('id', item_id)])
    return response.get('getExtendedMetadataResult', None)