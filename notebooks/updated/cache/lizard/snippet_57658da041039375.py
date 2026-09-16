def unarchive(self, target_path=None, zip_path=None):
    if target_path:
        self.target_path = target_path
    if zip_path:
        self.zip_path = zip_path
    if self.has_path is False:
        raise RuntimeError('')
    if os.path.isdir(self.target_path) is False:
        os.mkdir(self.target_path)
    with zipfile.ZipFile(self.zip_path, 'r') as zip:
        zip.extractall(self.target_path)