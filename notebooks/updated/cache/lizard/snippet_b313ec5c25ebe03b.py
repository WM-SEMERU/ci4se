def _BuildFindSpecsFromArtifact(self, definition, environment_variables):
    find_specs = []
    for source in definition.sources:
        if source.type_indicator == artifact_types.TYPE_INDICATOR_FILE:
            for path_entry in set(source.paths):
                specifications = self._BuildFindSpecsFromFileSourcePath(
                    path_entry, source.separator, environment_variables,
                    self._knowledge_base.user_accounts)
                find_specs.extend(specifications)
                self.file_system_artifact_names.add(definition.name)
        elif source.type_indicator == artifact_types.TYPE_INDICATOR_WINDOWS_REGISTRY_KEY:
            for key_path in set(source.keys):
                if ArtifactDefinitionsFilterHelper.CheckKeyCompatibility(
                    key_path):
                    specifications = self._BuildFindSpecsFromRegistrySourceKey(
                        key_path)
                    find_specs.extend(specifications)
                    self.registry_artifact_names.add(definition.name)
        elif source.type_indicator == artifact_types.TYPE_INDICATOR_WINDOWS_REGISTRY_VALUE:
            key_paths = {key_value['key'] for key_value in source.
                key_value_pairs}
            key_paths_string = ', '.join(key_paths)
            logger.warning(
                'Windows Registry values are not supported, extracting keys: "{0!s}"'
                .format(key_paths_string))
            for key_path in key_paths:
                if ArtifactDefinitionsFilterHelper.CheckKeyCompatibility(
                    key_path):
                    specifications = self._BuildFindSpecsFromRegistrySourceKey(
                        key_path)
                    find_specs.extend(specifications)
                    self.registry_artifact_names.add(definition.name)
        elif source.type_indicator == artifact_types.TYPE_INDICATOR_ARTIFACT_GROUP:
            for name in source.names:
                specifications = self._BuildFindSpecsFromGroupName(name,
                    environment_variables)
                find_specs.extend(specifications)
        else:
            logger.warning(
                'Unsupported artifact definition source type: "{0:s}"'.
                format(source.type_indicator))
    return find_specs