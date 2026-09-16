def BuildStats(self):
    artifact_reader = reader.YamlArtifactsReader()
    self.label_counts = {}
    self.os_counts = {}
    self.path_count = 0
    self.reg_key_count = 0
    self.source_type_counts = {}
    self.total_count = 0
    for artifact_definition in artifact_reader.ReadDirectory('data'):
        if hasattr(artifact_definition, 'labels'):
            for label in artifact_definition.labels:
                self.label_counts[label] = self.label_counts.get(label, 0) + 1
        for source in artifact_definition.sources:
            self.total_count += 1
            source_type = source.type_indicator
            self.source_type_counts[source_type] = self.source_type_counts.get(
                source_type, 0) + 1
            if source_type == definitions.TYPE_INDICATOR_WINDOWS_REGISTRY_KEY:
                self.reg_key_count += len(source.keys)
            elif source_type == definitions.TYPE_INDICATOR_WINDOWS_REGISTRY_VALUE:
                self.reg_key_count += len(source.key_value_pairs)
            elif source_type in (definitions.TYPE_INDICATOR_FILE,
                definitions.TYPE_INDICATOR_DIRECTORY):
                self.path_count += len(source.paths)
            os_list = source.supported_os
            for os_str in os_list:
                self.os_counts[os_str] = self.os_counts.get(os_str, 0) + 1