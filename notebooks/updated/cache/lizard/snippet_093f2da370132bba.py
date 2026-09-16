def extract_archive(archive, verbosity=0, outdir=None, program=None,
    interactive=True):
    util.check_existing_filename(archive)
    if verbosity >= 0:
        util.log_info('Extracting %s ...' % archive)
    return _extract_archive(archive, verbosity=verbosity, interactive=
        interactive, outdir=outdir, program=program)