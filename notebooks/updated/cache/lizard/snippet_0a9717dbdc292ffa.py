def resize_volume(self, size):
    curr_size = self.volume.size
    if size <= curr_size:
        raise exc.InvalidVolumeResize(
            "The new volume size must be larger than the current volume size of '%s'."
             % curr_size)
    body = {'volume': {'size': size}}
    self.manager.action(self, 'resize', body=body)