def load_merge_candidate(self, filename=None, config=None):
    self.config_replace = False
    return_status, msg = self._load_candidate_wrapper(source_file=filename,
        source_config=config, dest_file=self.merge_cfg, file_system=self.
        dest_file_system)
    if not return_status:
        raise MergeConfigException(msg)