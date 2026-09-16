def always_executed_hook(self):
    _logT = self._devProxy.get_logging_target()
    if 'device::sip_sdp_logger' not in _logT:
        try:
            self._devProxy.add_logging_target('device::sip_sdp/elt/logger')
            self.info_stream("Test of Tango logging from 'tc_tango_master'")
        except Exception as e:
            LOG.debug('Failed to setup Tango logging %s', e)