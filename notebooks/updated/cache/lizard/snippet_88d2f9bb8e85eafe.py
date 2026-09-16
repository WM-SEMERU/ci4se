def sync_config(self, force=False):
    from ambry.library.config import LibraryConfigSyncProxy
    lcsp = LibraryConfigSyncProxy(self)
    lcsp.sync(force=force)