def replace_drive_enclosure(self, information):
    uri = '{}/replaceDriveEnclosure'.format(self.data['uri'])
    result = self._helper.create(information, uri)
    self.refresh()
    return result