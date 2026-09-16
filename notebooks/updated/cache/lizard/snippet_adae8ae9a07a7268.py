def rmtree(self, ignore_errors=False, onerror=None):
    if not os.path.exists(self.workdir):
        return
    shutil.rmtree(self.workdir, ignore_errors=ignore_errors, onerror=onerror)