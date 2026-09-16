def check_repository_existence(params):
    repodir = os.path.join(params.outdir, params.name)
    if os.path.isdir(repodir):
        raise Conflict('Package repository "{0}" has already exists.'.
            format(repodir))