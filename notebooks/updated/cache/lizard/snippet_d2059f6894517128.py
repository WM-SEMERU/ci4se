def mkpartfs(device, part_type, fs_type, start, end):
    _validate_device(device)
    if part_type not in set(['primary', 'logical', 'extended']):
        raise CommandExecutionError(
            'Invalid part_type passed to partition.mkpartfs')
    if not _is_fstype(fs_type):
        raise CommandExecutionError(
            'Invalid fs_type passed to partition.mkpartfs')
    _validate_partition_boundary(start)
    _validate_partition_boundary(end)
    cmd = 'parted -m -s -- {0} mkpart {1} {2} {3} {4}'.format(device,
        part_type, fs_type, start, end)
    out = __salt__['cmd.run'](cmd).splitlines()
    return out