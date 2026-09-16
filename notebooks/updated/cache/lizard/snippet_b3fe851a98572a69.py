def _SetupBotoConfig(self):
    project_id = self._GetNumericProjectId()
    try:
        boto_config.BotoConfig(project_id, debug=self.debug)
    except (IOError, OSError) as e:
        self.logger.warning(str(e))