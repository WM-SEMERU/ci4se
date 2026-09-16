def _PreprocessSources(self, extraction_engine):
    logger.debug('Starting preprocessing.')
    try:
        artifacts_registry = engine.BaseEngine.BuildArtifactsRegistry(self.
            _artifact_definitions_path, self._custom_artifacts_path)
        extraction_engine.PreprocessSources(artifacts_registry, self.
            _source_path_specs, resolver_context=self._resolver_context)
    except IOError as exception:
        logger.error('Unable to preprocess with error: {0!s}'.format(exception)
            )
    logger.debug('Preprocessing done.')