def make_apps_dir(self):
    self.logger.info(
        'Creating a directory for symlinks to your Django applications `%s` ...'
         % self.apps_path)
    try:
        os.mkdir(self.apps_path)
    except OSError:
        pass
    return self.apps_path