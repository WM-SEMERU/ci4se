def checksum_status(self, filename):
    return self.upload_service.api_client.checksum_status(area_uuid=self.
        uuid, filename=filename)