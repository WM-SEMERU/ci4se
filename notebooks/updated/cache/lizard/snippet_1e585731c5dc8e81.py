def _clear_mountpoint(self):
    if self.mountpoint:
        os.rmdir(self.mountpoint)
        self.mountpoint = ''