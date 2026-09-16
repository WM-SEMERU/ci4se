def log_file(self):
    log_file = self.get('log')
    if not log_file:
        log_file = '%s.log' % self.name
        self.set('log', log_file)
    return os.path.join(self.initial_dir, self.get('log'))