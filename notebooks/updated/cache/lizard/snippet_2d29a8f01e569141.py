def extract_dms(archive, compression, cmd, verbosity, interactive, outdir):
    check_archive_ext(archive)
    cmdlist = [cmd, '-d', outdir]
    if verbosity > 1:
        cmdlist.append('-v')
    cmdlist.extend(['u', archive])
    return cmdlist