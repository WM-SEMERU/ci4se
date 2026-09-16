def LVMPathSpecGetVolumeIndex(path_spec):
    volume_index = getattr(path_spec, 'volume_index', None)
    if volume_index is None:
        location = getattr(path_spec, 'location', None)
        if location is None or not location.startswith('/lvm'):
            return None
        volume_index = None
        try:
            volume_index = int(location[4:], 10) - 1
        except ValueError:
            pass
        if volume_index is None or volume_index < 0:
            return None
    return volume_index