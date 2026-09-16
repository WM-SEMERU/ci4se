def area_uri(self, area_uuid):
    if area_uuid not in self.areas:
        raise UploadException("I don't know about area {uuid}".format(uuid=
            area_uuid))
    return UploadAreaURI(self._config.upload.areas[area_uuid]['uri'])