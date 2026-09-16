def linkorcopy(self, src, dst):
    if os.path.isdir(dst):
        log.warn('linkorcopy given a directory as destination. Use caution.')
        log.debug('src: %s  dst: %s', src, dst)
    elif os.path.exists(dst):
        os.unlink(dst)
    elif not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    if self.linkfiles:
        log.debug('Linking: %s -> %s', src, dst)
        os.link(src, dst)
    else:
        log.debug('Copying: %s -> %s', src, dst)
        shutil.copy2(src, dst)