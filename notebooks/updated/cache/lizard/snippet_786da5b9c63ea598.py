def zfs():
    grains = {}
    grains['zfs_support'] = __utils__['zfs.is_supported']()
    grains['zfs_feature_flags'] = __utils__['zfs.has_feature_flags']()
    if grains['zfs_support']:
        grains = salt.utils.dictupdate.update(grains, _zfs_pool_data(),
            merge_lists=True)
    return grains