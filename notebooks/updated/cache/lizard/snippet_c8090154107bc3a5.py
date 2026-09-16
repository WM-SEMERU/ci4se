def _check_disks_in_diskgroup(disk_group, cache_disk_id, capacity_disk_ids):
    if not disk_group.ssd.canonicalName == cache_disk_id:
        raise salt.exceptions.ArgumentValueError(
            "Incorrect diskgroup cache disk; got id: '{0}'; expected id: '{1}'"
            .format(disk_group.ssd.canonicalName, cache_disk_id))
    non_ssd_disks = [d.canonicalName for d in disk_group.nonSsd]
    if sorted(non_ssd_disks) != sorted(capacity_disk_ids):
        raise salt.exceptions.ArgumentValueError(
            "Incorrect capacity disks; got ids: '{0}'; expected ids: '{1}'"
            .format(sorted(non_ssd_disks), sorted(capacity_disk_ids)))
    log.trace("Checked disks in diskgroup with cache disk id '%s'",
        cache_disk_id)
    return True