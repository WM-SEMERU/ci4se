def add_to_manifest(self, manifest):
    manifest.add_service(self.service.name)
    manifest.write_manifest()