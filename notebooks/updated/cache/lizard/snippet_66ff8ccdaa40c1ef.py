def download_apk(self, path='.'):
    apk_fd, apk_fn = tempfile.mkstemp(prefix='fuzzfetch-', suffix='.apk')
    os.close(apk_fd)
    try:
        _download_url(self.artifact_url('apk'), apk_fn)
        shutil.copy(apk_fn, os.path.join(path, 'target.apk'))
    finally:
        os.unlink(apk_fn)