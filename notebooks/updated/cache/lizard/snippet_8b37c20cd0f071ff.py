def _parse_config(self, requires_cfg=True):
    if len(self.config_paths) > 0:
        try:
            self._find_config()
        except BisonError:
            if not requires_cfg:
                return
            raise
        try:
            with open(self.config_file, 'r') as f:
                parsed = self._fmt_to_parser[self.config_format](f)
        except Exception as e:
            raise BisonError('Failed to parse config file: {}'.format(self.
                config_file)) from e
        self._full_config = None
        self._config = parsed