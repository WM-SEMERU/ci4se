def open(self):
    safe_mkdir(os.path.dirname(self._html_dir))
    self._report_file = open(self.report_path(), 'w')