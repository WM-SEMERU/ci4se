def _convert_volume_from(self, volume_from):
    if ':' in volume_from:
        container, permissions = volume_from.split(':')
    else:
        container = volume_from
        permissions = 'rw'
    if permissions not in ('ro', 'rw'):
        raise ValueError(
            'only permissions supported for volumes_from are rw and ro.')
    return '{0}:{1}'.format(container, permissions)