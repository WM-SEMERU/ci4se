def update_firmware(self, firmware_information, force=False):
    firmware_uri = '{}/firmware'.format(self.data['uri'])
    result = self._helper.update(firmware_information, firmware_uri, force=
        force)
    self.refresh()
    return result