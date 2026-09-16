def BuildFindSpecs(self, artifact_filter_names, environment_variables=None):
    find_specs = []
    for name in artifact_filter_names:
        definition = self._artifacts_registry.GetDefinitionByName(name)
        if not definition:
            logger.debug('undefined artifact definition: {0:s}'.format(name))
            continue
        logger.debug('building find spec from artifact definition: {0:s}'.
            format(name))
        artifact_find_specs = self._BuildFindSpecsFromArtifact(definition,
            environment_variables)
        find_specs.extend(artifact_find_specs)
    for find_spec in find_specs:
        if isinstance(find_spec, file_system_searcher.FindSpec):
            self.file_system_find_specs.append(find_spec)
        elif isinstance(find_spec, registry_searcher.FindSpec):
            self.registry_find_specs.append(find_spec)
        else:
            logger.warning('Unsupported find specification type: {0:s}'.
                format(type(find_spec)))