def set_resolved_url(self, item=None, subtitles=None):
    if self._end_of_directory:
        raise Exception(
            'Current XBMC handle has been removed. Either set_resolved_url(), end_of_directory(), or finish() has already been called.'
            )
    self._end_of_directory = True
    succeeded = True
    if item is None:
        item = {}
        succeeded = False
    if isinstance(item, basestring):
        item = {'path': item}
    item = self._listitemify(item)
    item.set_played(True)
    xbmcplugin.setResolvedUrl(self.handle, succeeded, item.as_xbmc_listitem())
    if subtitles:
        self._add_subtitles(subtitles)
    return [item]