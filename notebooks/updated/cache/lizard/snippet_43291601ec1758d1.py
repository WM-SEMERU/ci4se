def extract_lrzip(archive, compression, cmd, verbosity, interactive, outdir):
    cmdlist = [cmd, '-d']
    if verbosity > 1:
        cmdlist.append('-v')
    outfile = util.get_single_outfile(outdir, archive)
    cmdlist.extend(['-o', outfile, os.path.abspath(archive)])
    return cmdlist