def archive(self, target_path=None, zip_path=None):
    if target_path:
        self.target_path = target_path
    if zip_path:
        self.zip_path = zip_path
    if self.has_path is False or os.path.isdir(self.target_path) is False:
        raise RuntimeError('')
    zip = zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED)
    for root, _, files in os.walk(self.target_path):
        for file in files:
            if file in ARCHIVE_IGNORE_FILES:
                continue
            current_dir = os.path.relpath(root, self.target_path)
            if current_dir == '.':
                file_path = file
            else:
                file_path = os.path.join(current_dir, file)
            print('Archive {}'.format(file))
            zip.write(os.path.join(root, file), file_path)
    zip.close()