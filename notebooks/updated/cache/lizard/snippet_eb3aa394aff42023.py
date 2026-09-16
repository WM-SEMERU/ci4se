def can_accomodate(self, logical_disk):
    raid_level = constants.RAID_LEVEL_INPUT_TO_HPSSA_MAPPING.get(logical_disk
        ['raid_level'], logical_disk['raid_level'])
    args = ('array', self.id, 'create', 'type=logicaldrive', 'raid=%s' %
        raid_level, 'size=?')
    if logical_disk['size_gb'] != 'MAX':
        desired_disk_size = logical_disk['size_gb']
    else:
        desired_disk_size = constants.MINIMUM_DISK_SIZE
    try:
        stdout, stderr = self.parent.execute_cmd(*args,
            dont_transform_to_hpssa_exception=True)
    except processutils.ProcessExecutionError as ex:
        if ex.exit_code == 1:
            return False
        else:
            raise exception.HPSSAOperationError(reason=ex)
    except Exception as ex:
        raise exception.HPSSAOperationError(reason=ex)
    match = re.search('Max: (\\d+)', stdout)
    if not match:
        return False
    max_size_gb = int(match.group(1)) / 1024
    return desired_disk_size <= max_size_gb