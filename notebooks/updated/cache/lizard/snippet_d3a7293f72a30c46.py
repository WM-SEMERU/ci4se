def get_ignored_files(self):
    return [os.path.join(self.path, p) for p in self.run('ls-files',
        '--ignored', '--exclude-standard', '--others').strip().split()]