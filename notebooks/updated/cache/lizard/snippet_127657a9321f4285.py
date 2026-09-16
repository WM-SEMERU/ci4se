def GetFileEntryByPathSpec(self, path_spec):
    tsk_vs_part, partition_index = tsk_partition.GetTSKVsPartByPathSpec(self
        ._tsk_volume, path_spec)
    location = getattr(path_spec, 'location', None)
    if tsk_vs_part is None:
        if location is None or location != self.LOCATION_ROOT:
            return None
        return tsk_partition_file_entry.TSKPartitionFileEntry(self.
            _resolver_context, self, path_spec, is_root=True, is_virtual=True)
    if location is None and partition_index is not None:
        path_spec.location = '/p{0:d}'.format(partition_index)
    return tsk_partition_file_entry.TSKPartitionFileEntry(self.
        _resolver_context, self, path_spec)