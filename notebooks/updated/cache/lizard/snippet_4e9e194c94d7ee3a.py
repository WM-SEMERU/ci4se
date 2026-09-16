def get_table_metadata(self, resource, resource_class):
    return self._make_metadata_request(meta_id=resource + ':' +
        resource_class, metadata_type='METADATA-TABLE')