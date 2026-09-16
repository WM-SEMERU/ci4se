def metadata_extractor(self):
    if not hasattr(self, '_local_file'):
        raise AttributeError(
            'local_file attribute must be set before calling metadata_extractor'
            )
    if not hasattr(self, '_metadata_extractor'):
        if self.local_file.endswith('.whl'):
            logger.info(
                'Getting metadata from wheel using WheelMetadataExtractor.')
            extractor_cls = metadata_extractors.WheelMetadataExtractor
        else:
            logger.info(
                'Getting metadata from setup.py using SetupPyMetadataExtractor.'
                )
            extractor_cls = metadata_extractors.SetupPyMetadataExtractor
        base_python_version = (self.base_python_version or self.
            template_base_py_ver)
        self._metadata_extractor = extractor_cls(self.local_file, self.name,
            self.name_convertor, self.version, self.rpm_name, self.venv,
            base_python_version)
    return self._metadata_extractor