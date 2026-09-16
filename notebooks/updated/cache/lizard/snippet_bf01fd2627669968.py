def has_sources(self, extension=None):
    source_paths = self._sources_field.source_paths
    if not source_paths:
        return False
    if not extension:
        return True
    return any(source.endswith(extension) for source in source_paths)