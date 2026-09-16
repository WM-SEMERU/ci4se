def _save_cb(self, w):
    format = self.saved_type
    if format is None:
        return self.fv.show_error('Please save an image first.')
    filename = self.w.name.get_text().strip()
    if len(filename) == 0:
        return self.fv.show_error('Please set a name for saving the file')
    self.save_name = filename
    if not filename.lower().endswith('.' + format):
        filename = filename + '.' + format
    path = self.w.folder.get_text().strip()
    if path == '':
        path = filename
    else:
        self.save_path = path
        path = os.path.join(path, filename)
    self.fv.error_wrap(shutil.copyfile, self.tmpname, path)