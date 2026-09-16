def delete(self):
    versions = self.get_versions()
    self.api.manager.delete_archive_record(self.archive_name)
    for version in versions:
        if self.authority.fs.exists(self.get_version_path(version)):
            self.authority.fs.remove(self.get_version_path(version))
        if self.api.cache:
            if self.api.cache.fs.exists(self.get_version_path(version)):
                self.api.cache.fs.remove(self.get_version_path(version))
    if self.authority.fs.exists(self.archive_name):
        self.authority.fs.removedir(self.archive_name)
    if self.api.cache:
        if self.api.cache.fs.exists(self.archive_name):
            self.api.cache.fs.removedir(self.archive_name)