def DeregisterMountPoint(cls, mount_point):
    if mount_point not in cls._mount_points:
        raise KeyError('Mount point: {0:s} not set.'.format(mount_point))
    del cls._mount_points[mount_point]