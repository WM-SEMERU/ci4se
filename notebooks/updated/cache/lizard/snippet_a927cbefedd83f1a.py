def _ParseFileData(self, knowledge_base, file_object):
    plist_file = plist.PlistFile()
    try:
        plist_file.Read(file_object)
    except IOError as exception:
        raise errors.PreProcessFail('Unable to read: {0:s} with error: {1!s}'
            .format(self.ARTIFACT_DEFINITION_NAME, exception))
    if not plist_file.root_key:
        raise errors.PreProcessFail(
            'Unable to read: {0:s} with error: missing root key'.format(
            self.ARTIFACT_DEFINITION_NAME))
    matches = []
    self._FindKeys(plist_file.root_key, self._PLIST_KEYS, matches)
    if not matches:
        raise errors.PreProcessFail(
            'Unable to read: {0:s} with error: no such keys: {1:s}.'.format
            (self.ARTIFACT_DEFINITION_NAME, ', '.join(self._PLIST_KEYS)))
    name = None
    value = None
    for name, value in matches:
        if value:
            break
    if value is None:
        raise errors.PreProcessFail(
            'Unable to read: {0:s} with error: no values found for keys: {1:s}.'
            .format(self.ARTIFACT_DEFINITION_NAME, ', '.join(self._PLIST_KEYS))
            )
    self._ParsePlistKeyValue(knowledge_base, name, value)