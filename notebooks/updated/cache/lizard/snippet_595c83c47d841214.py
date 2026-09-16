def setup(self):
    decompress_dir('.')
    if self.backup:
        for f in FEFF_INPUT_FILES:
            shutil.copy(f, '{}.orig'.format(f))
        for f in FEFF_BACKUP_FILES:
            if os.path.isfile(f):
                shutil.copy(f, '{}.orig'.format(f))