def mainloop(self):
    if not self.args:
        self.parser.print_help()
        self.parser.exit()
    elif len(self.args) < 1:
        self.parser.error('Expecting at least a metafile name')
    metapath = self.args[0]
    try:
        metainfo = bencode.bread(metapath)
    except (KeyError, bencode.BencodeError) as exc:
        self.LOG.error('Bad metafile %r (%s: %s)' % (metapath, type(exc).
            __name__, exc))
    else:
        try:
            metafile.check_meta(metainfo)
        except ValueError as exc:
            self.LOG.error('Metafile %r failed integrity check: %s' % (
                metapath, exc))
        else:
            if len(self.args) > 1:
                datapath = self.args[1].rstrip(os.sep)
            else:
                datapath = metainfo['info']['name']
            torrent = metafile.Metafile(metapath)
            torrent.check(metainfo, datapath, progress=None if self.options
                .quiet else metafile.console_progress())