def create_patch(self, patch_name):
    patch_path = self._get_patch_path(patch_name)
    if os.path.exists(patch_path):
        raise StashException("patch '%s' already exists" % patch_name)
    patch = self.repository.diff()
    if patch != '':
        patch_file = open(patch_path, 'wb')
        patch_file.write(patch.encode('utf-8'))
        patch_file.close()
        pre_file_status = self.repository.status()
        self.repository.revert_all()
        changed_file_status = self.repository.status().difference(
            pre_file_status)
        for status, file_name in changed_file_status:
            if status == FileStatus.Added:
                os.unlink(os.path.join(self.repository.root_path, file_name))
    return patch != ''