def extract_chm(archive, compression, cmd, verbosity, interactive, outdir):
    name = util.get_single_outfile('', archive)
    outfile = os.path.join(outdir, name)
    return [cmd, '-x', os.path.abspath(archive), outfile]