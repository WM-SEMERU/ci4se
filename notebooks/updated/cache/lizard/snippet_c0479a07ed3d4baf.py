def purge_metadata_by_name(self, name):
    meta_dir = self._get_metadata_dir_by_name(name, self._metadata_base_dir)
    logger.debug('purging metadata directory: {}'.format(meta_dir))
    try:
        rm_rf(meta_dir)
    except OSError as e:
        raise ProcessMetadataManager.MetadataError(
            'failed to purge metadata directory {}: {!r}'.format(meta_dir, e))