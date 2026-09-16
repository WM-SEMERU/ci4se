def get_firmware_manifest(self, manifest_id):
    api = self._get_api(update_service.DefaultApi)
    return FirmwareManifest(api.firmware_manifest_retrieve(manifest_id=
        manifest_id))