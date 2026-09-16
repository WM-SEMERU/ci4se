def save_neighbour_info(self, cache_dir, mask=None, **kwargs):
    if cache_dir:
        mask_name = getattr(mask, 'name', None)
        filename = self._create_cache_filename(cache_dir, mask=mask_name,
            **kwargs)
        LOG.info('Saving kd_tree neighbour info to %s', filename)
        cache = self._read_resampler_attrs()
        self._apply_cached_indexes(cache, persist=True)
        self._index_caches[mask_name] = cache
        np.savez(filename, **cache)