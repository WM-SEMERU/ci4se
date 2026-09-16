def list_subdirs(self, container, marker=None, limit=None, prefix=None,
    delimiter=None, full_listing=False):
    mthd = container.list_all if full_listing else container.list
    objs = mthd(marker=marker, limit=limit, prefix=prefix, delimiter='/',
        return_raw=True)
    sdirs = [obj for obj in objs if 'subdir' in obj]
    mgr = container.object_manager
    return [StorageObject(mgr, sdir) for sdir in sdirs]