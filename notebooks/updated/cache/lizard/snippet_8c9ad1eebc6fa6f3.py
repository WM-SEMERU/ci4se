def _finalize(self, dry_run=False):
    for rmfile in self.files.temp_files:
        if dry_run:
            print('remove %s' % rmfile)
        else:
            os.remove(rmfile)
    for gzfile in self.files.gzip_files:
        if dry_run:
            pass
        else:
            os.system('gzip -9 %s' % gzfile)