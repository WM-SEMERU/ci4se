def partition_dumps(self):
    manifest = self.manifest_class()
    manifest_size = 0
    manifest_files = 0
    for resource in self.resources:
        manifest.add(resource)
        manifest_size += resource.length
        manifest_files += 1
        if manifest_size >= self.max_size or manifest_files >= self.max_files:
            yield manifest
            manifest = self.manifest_class()
            manifest_size = 0
            manifest_files = 0
    if manifest_files > 0:
        yield manifest