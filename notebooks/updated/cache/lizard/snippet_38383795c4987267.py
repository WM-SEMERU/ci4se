def _convert_volume(self, volume):
    data = {'host': volume.get('hostPath'), 'container': volume.get(
        'containerPath'), 'readonly': volume.get('mode') == 'RO'}
    return data