def _add_vrfs(self, settings):
    for vrf_settings in settings:
        LOG.debug('Adding VRF settings: %s', vrf_settings)
        try:
            self.speaker.vrf_add(**vrf_settings)
        except RuntimeConfigError as e:
            LOG.exception(e)