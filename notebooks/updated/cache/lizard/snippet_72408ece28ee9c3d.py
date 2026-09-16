def add_tar_opts(cmdlist, compression, verbosity):
    progname = os.path.basename(cmdlist[0])
    if compression == 'gzip':
        cmdlist.append('-z')
    elif compression == 'compress':
        cmdlist.append('-Z')
    elif compression == 'bzip2':
        cmdlist.append('-j')
    elif compression in ('lzma', 'xz') and progname == 'bsdtar':
        cmdlist.append('--%s' % compression)
    elif compression in ('lzma', 'xz', 'lzip'):
        program = compression
        cmdlist.extend(['--use-compress-program', program])
    if verbosity > 1:
        cmdlist.append('--verbose')
    if progname == 'tar':
        cmdlist.append('--force-local')