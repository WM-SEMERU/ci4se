def make_archive(self, path):
    zf = zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(self.path):
        relative_path = dirpath[len(self.path) + 1:]
        if relative_path and not self._ignore(relative_path):
            zf.write(dirpath, relative_path)
        for name in filenames:
            archive_name = os.path.join(relative_path, name)
            if not self._ignore(archive_name):
                real_path = os.path.join(dirpath, name)
                self._check_type(real_path)
                if os.path.islink(real_path):
                    self._check_link(real_path)
                    self._write_symlink(zf, os.readlink(real_path),
                        archive_name)
                else:
                    zf.write(real_path, archive_name)
    zf.close()
    return path