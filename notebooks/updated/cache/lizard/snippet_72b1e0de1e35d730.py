def _ParseVolumeIdentifiersString(self, volume_identifiers_string, prefix='v'):
    prefix_length = 0
    if prefix:
        prefix_length = len(prefix)
    if not volume_identifiers_string:
        return []
    if volume_identifiers_string == 'all':
        return ['all']
    volume_identifiers = set()
    for identifiers_range in volume_identifiers_string.split(','):
        if '..' in identifiers_range:
            first_identifier, last_identifier = identifiers_range.split('..')
            if first_identifier.startswith(prefix):
                first_identifier = first_identifier[prefix_length:]
            if last_identifier.startswith(prefix):
                last_identifier = last_identifier[prefix_length:]
            try:
                first_identifier = int(first_identifier, 10)
                last_identifier = int(last_identifier, 10)
            except ValueError:
                raise ValueError('Invalid volume identifiers range: {0:s}.'
                    .format(identifiers_range))
            for volume_identifier in range(first_identifier, 
                last_identifier + 1):
                if volume_identifier not in volume_identifiers:
                    volume_identifier = '{0:s}{1:d}'.format(prefix,
                        volume_identifier)
                    volume_identifiers.add(volume_identifier)
        else:
            identifier = identifiers_range
            if identifier.startswith(prefix):
                identifier = identifiers_range[prefix_length:]
            try:
                volume_identifier = int(identifier, 10)
            except ValueError:
                raise ValueError('Invalid volume identifier range: {0:s}.'.
                    format(identifiers_range))
            volume_identifier = '{0:s}{1:d}'.format(prefix, volume_identifier)
            volume_identifiers.add(volume_identifier)
    return sorted(volume_identifiers)