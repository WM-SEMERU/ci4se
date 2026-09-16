def enable_extended_scan_code_mode(self):
    if not self.capabilities.have_extended_scan_code_mode():
        raise
    self._require_version(major=2)
    self.config_flag('SHORT_TICKET', True)
    self.config_flag('STATIC_TICKET', False)