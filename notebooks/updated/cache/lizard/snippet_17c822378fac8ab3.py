def get_root(self, drive):
    drive = _my_normcase(drive)
    try:
        return self.Root[drive]
    except KeyError:
        root = RootDir(drive, self)
        self.Root[drive] = root
        if not drive:
            self.Root[self.defaultDrive] = root
        elif drive == self.defaultDrive:
            self.Root[''] = root
        return root