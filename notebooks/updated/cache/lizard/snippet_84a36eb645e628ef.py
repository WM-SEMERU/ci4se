def get_extra_managed_storage_volume_paths(self, start=0, count=-1, filter=
    '', sort=''):
    uri = self.URI + '/repair?alertFixType=ExtraManagedStorageVolumePaths'
    return self._client.get_all(start, count, filter=filter, sort=sort, uri=uri
        )