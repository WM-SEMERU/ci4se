def SetExtractionConfiguration(self, configuration):
    self._hasher_file_size_limit = configuration.hasher_file_size_limit
    self._SetHashers(configuration.hasher_names_string)
    self._process_archives = configuration.process_archives
    self._process_compressed_streams = configuration.process_compressed_streams
    self._SetYaraRules(configuration.yara_rules_string)