def get_firmware_update_progress(self):
    try:
        self.refresh()
    except sushy.exceptions.SushyError as e:
        msg = 'Progress of firmware update not known. Error %(error)s' % {
            'error': str(e)}
        LOG.debug(msg)
        return 'Unknown', 'Unknown'
    return self.firmware_state, self.firmware_percentage