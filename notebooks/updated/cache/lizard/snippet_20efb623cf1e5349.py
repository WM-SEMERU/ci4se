def sync_out(self, release):
    if release.get('rsync_out_objs'):
        tree = release['canonical_dir']
        if not os.path.isdir(tree):
            self.log.info('Creating %s', tree)
            os.makedirs(tree)
        self.call(release['rsync_out_objs'])
        self.call(release['rsync_out_rest'])