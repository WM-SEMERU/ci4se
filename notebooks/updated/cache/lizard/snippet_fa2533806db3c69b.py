def _delete_stale(self):
    for name, hash_ in self._stale_files.items():
        path = self.download_root.joinpath(name)
        if not path.exists():
            continue
        current_hash = self._path_hash(path)
        if current_hash == hash_:
            progress_logger.info('deleting: %s which is stale...', name)
            path.unlink()
            self._stale_deleted += 1
            while True:
                path = path.parent
                if path == self.download_root or list(path.iterdir()):
                    break
                progress_logger.info('deleting: %s which is stale..', path.
                    relative_to(self.download_root))
                path.rmdir()
        else:
            progress_logger.error(
                'Not deleting "%s" which is in the lock file but not the definition file, however appears to have been modified since it was downloaded. Please check and delete the file manually.'
                , name)
            raise GrablibError('stale file modified')