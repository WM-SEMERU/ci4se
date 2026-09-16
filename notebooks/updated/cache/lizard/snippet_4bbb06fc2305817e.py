def dep(self, source_name):
    from ambry.orm.exc import NotFoundError
    from ambry.dbexceptions import ConfigurationError
    source = self.source(source_name)
    ref = source.url
    if not ref:
        raise ValueError("Got an empty ref for source '{}' ".format(source.
            name))
    try:
        try:
            p = self.library.partition(ref)
        except NotFoundError:
            self.warn('Partition reference {} not found, try to download it'
                .format(ref))
            remote, vname = self.library.find_remote_bundle(ref, try_harder
                =True)
            if remote:
                self.warn('Installing {} from {}'.format(remote, vname))
                self.library.checkin_remote_bundle(vname, remote)
                p = self.library.partition(ref)
            else:
                raise
        if not p.is_local:
            with self.progress.start('test', 0, message='localizing') as ps:
                p.localize(ps)
        return p
    except NotFoundError:
        return self.library.bundle(ref)