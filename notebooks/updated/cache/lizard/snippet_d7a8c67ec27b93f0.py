def slice(self, rng, num_of_slices=None, slice_pos=None, slice_start=None,
    slice_end=None, cache_dir=None):
    if (num_of_slices is not None and slice_pos is not None and slice_start is
        None and slice_end is None):
        size = self._size // num_of_slices
        amount = self._size % num_of_slices
        slice_start = slice_pos * size
        if slice_pos < amount:
            slice_start += slice_pos
        else:
            slice_start += amount
        slice_end = slice_start + size
        if slice_end > self._size:
            slice_start -= slice_end - self._size
            slice_end = self._size
    elif num_of_slices is None and slice_pos is None and slice_start is not None and slice_end is not None:
        pass
    else:
        logger.critical(
            'You must specify position(num_of_slice and slice_pos) or range(slice_start and slice_end).'
            )
        return None
    if cache_dir is None:
        ds = self._data_source
        while '_data_source' in dir(ds):
            if '_cache_dir' in dir(ds):
                cache_dir = ds._cache_dir
            ds = ds._data_source
    if cache_dir is None:
        return DataIterator(DataSourceWithMemoryCache(SlicedDataSource(self
            ._data_source, self._data_source.shuffle, slice_start=
            slice_start, slice_end=slice_end), shuffle=self._shuffle, rng=
            rng), self._batch_size)
    else:
        return DataIterator(DataSourceWithMemoryCache(
            DataSourceWithFileCache(SlicedDataSource(self._data_source,
            self._data_source.shuffle, slice_start=slice_start, slice_end=
            slice_end), cache_dir=cache_dir, cache_file_name_prefix=
            'cache_sliced_{:08d}_{:08d}'.format(slice_start, slice_end),
            shuffle=self._shuffle, rng=rng), shuffle=self._shuffle, rng=rng
            ), self._batch_size)