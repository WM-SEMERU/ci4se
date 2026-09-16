def is_handleable(self, device):
    ignored = self._ignore_device(device)
    if ignored is None and device is not None:
        return self.is_handleable(_get_parent(device))
    return not ignored