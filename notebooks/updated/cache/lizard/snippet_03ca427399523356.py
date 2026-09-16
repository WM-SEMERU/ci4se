def _GetVSSStoreIdentifiers(self, scan_node):
    if not scan_node or not scan_node.path_spec:
        raise errors.SourceScannerError('Invalid scan node.')
    volume_system = vshadow_volume_system.VShadowVolumeSystem()
    volume_system.Open(scan_node.path_spec)
    volume_identifiers = self._source_scanner.GetVolumeIdentifiers(
        volume_system)
    if not volume_identifiers:
        return []
    if self._vss_stores:
        if self._vss_stores == 'all':
            vss_stores = range(1, volume_system.number_of_volumes + 1)
        else:
            vss_stores = self._vss_stores
        selected_volume_identifiers = self._NormalizedVolumeIdentifiers(
            volume_system, vss_stores, prefix='vss')
        if not set(selected_volume_identifiers).difference(volume_identifiers):
            return selected_volume_identifiers
    try:
        volume_identifiers = self._PromptUserForVSSStoreIdentifiers(
            volume_system, volume_identifiers)
    except KeyboardInterrupt:
        raise errors.UserAbort('File system scan aborted.')
    return self._NormalizedVolumeIdentifiers(volume_system,
        volume_identifiers, prefix='vss')