def _ParseSourceType(self, source):
    type_name = rdf_artifacts.ArtifactSource.SourceType
    switch = {type_name.COMMAND: self._ProcessCommandSource, type_name.
        DIRECTORY: self._ProcessFileSource, type_name.FILE: self.
        _ProcessFileSource, type_name.GREP: self._ProcessGrepSource,
        type_name.REGISTRY_KEY: self._ProcessRegistryKeySource, type_name.
        REGISTRY_VALUE: self._ProcessRegistryValueSource, type_name.WMI:
        self._ProcessWmiSource, type_name.ARTIFACT_FILES: self.
        _ProcessArtifactFilesSource, type_name.GRR_CLIENT_ACTION: self.
        _ProcessClientActionSource}
    source_type = source.base_source.type
    try:
        source_type_action = switch[source_type]
    except KeyError:
        raise ValueError('Incorrect source type: %s' % source_type)
    for res in source_type_action(source):
        yield res