def archive_all_files(self, archiver):
    for file_path in self.extra:
        archiver(path.abspath(file_path), path.join(self.prefix, file_path))
    for file_path in self.walk_git_files():
        archiver(path.join(self.main_repo_abspath, file_path), path.join(
            self.prefix, file_path))