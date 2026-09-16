def _Open(self, path_spec=None, mode='rb'):
    if not path_spec:
        raise ValueError('Missing path specification.')
    if not path_spec.HasParent():
        raise errors.PathSpecError(
            'Unsupported path specification without parent.')
    self._file_system = resolver.Resolver.OpenFileSystem(path_spec,
        resolver_context=self._resolver_context)
    tsk_volume = self._file_system.GetTSKVolume()
    tsk_vs, _ = tsk_partition.GetTSKVsPartByPathSpec(tsk_volume, path_spec)
    if tsk_vs is None:
        raise errors.PathSpecError(
            'Unable to retrieve TSK volume system part from path specification.'
            )
    range_offset = tsk_partition.TSKVsPartGetStartSector(tsk_vs)
    range_size = tsk_partition.TSKVsPartGetNumberOfSectors(tsk_vs)
    if range_offset is None or range_size is None:
        raise errors.PathSpecError(
            'Unable to retrieve TSK volume system part data range from path specification.'
            )
    bytes_per_sector = tsk_partition.TSKVolumeGetBytesPerSector(tsk_volume)
    range_offset *= bytes_per_sector
    range_size *= bytes_per_sector
    self.SetRange(range_offset, range_size)
    self._file_object = resolver.Resolver.OpenFileObject(path_spec.parent,
        resolver_context=self._resolver_context)
    self._file_object_set_in_init = True
    super(TSKPartitionFile, self)._Open(path_spec=path_spec, mode=mode)