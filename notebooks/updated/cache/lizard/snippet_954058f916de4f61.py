def write_remote_map(self):
    remote_map = salt.utils.path.join(self.cache_root, 'remote_map.txt')
    try:
        with salt.utils.files.fopen(remote_map, 'w+') as fp_:
            timestamp = datetime.now().strftime('%d %b %Y %H:%M:%S.%f')
            fp_.write('# {0}_remote map as of {1}\n'.format(self.role,
                timestamp))
            for repo in self.remotes:
                fp_.write(salt.utils.stringutils.to_str('{0} = {1}\n'.
                    format(repo.cachedir_basename, repo.id)))
    except OSError:
        pass
    else:
        log.info('Wrote new %s remote map to %s', self.role, remote_map)