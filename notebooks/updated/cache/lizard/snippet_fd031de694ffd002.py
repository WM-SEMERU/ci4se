def update(self, filepath, cache=False, remove=False, bumpversion=None,
    prerelease=None, dependencies=None, metadata=None, message=None):
    if metadata is None:
        metadata = {}
    latest_version = self.get_latest_version()
    hashval = self.api.hash_file(filepath)
    checksum = hashval['checksum']
    algorithm = hashval['algorithm']
    if checksum == self.get_latest_hash():
        self.update_metadata(metadata)
        if remove and os.path.isfile(filepath):
            os.remove(filepath)
        return
    if self.versioned:
        if latest_version is None:
            latest_version = BumpableVersion()
        next_version = latest_version.bump(kind=bumpversion, prerelease=
            prerelease, inplace=False)
    else:
        next_version = None
    next_path = self.get_version_path(next_version)
    if cache:
        self.cache(next_version)
    if self.is_cached(next_version):
        self.authority.upload(filepath, next_path)
        self.api.cache.upload(filepath, next_path, remove=remove)
    else:
        self.authority.upload(filepath, next_path, remove=remove)
    self._update_manager(archive_metadata=metadata, version_metadata=dict(
        checksum=checksum, algorithm=algorithm, version=next_version,
        dependencies=dependencies, message=message))