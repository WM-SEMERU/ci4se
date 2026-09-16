def check_files(self, to_path=None):
    if to_path:
        target_path = os.path.normpath(os.path.realpath(to_path))
    else:
        target_path = os.getcwd()
    for filename in self.filenames():
        extract_path = os.path.join(target_path, filename)
        extract_path = os.path.normpath(os.path.realpath(extract_path))
        if not extract_path.startswith(target_path):
            raise UnsafeArchive(
                'Archive member destination is outside the target directory.  member: %s'
                 % filename)