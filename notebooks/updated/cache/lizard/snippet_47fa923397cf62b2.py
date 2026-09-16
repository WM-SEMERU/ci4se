def destroy(self):
    path = next(iter(self.linuxPaths))
    directory = _Directory(os.path.dirname(path))
    with directory as device:
        device.SNAP_DESTROY(name=str(os.path.basename(path)))