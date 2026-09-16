def clear_cache(self):
    errors = []
    for rdir in (self.cache_root, self.file_list_cachedir):
        if os.path.exists(rdir):
            try:
                shutil.rmtree(rdir)
            except OSError as exc:
                errors.append('Unable to delete {0}: {1}'.format(rdir, exc))
    return errors