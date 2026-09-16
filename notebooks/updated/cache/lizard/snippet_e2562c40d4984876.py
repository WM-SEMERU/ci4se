def _build_mountpoint(self, volume):
    self.add_volume(self._build_volume(volume))
    return {'sourceVolume': self.path_to_name(volume.get('host')),
        'containerPath': volume.get('container')}