def _SConstruct_exists(dirname='', repositories=[], filelist=None):
    if not filelist:
        filelist = ['SConstruct', 'Sconstruct', 'sconstruct']
    for file in filelist:
        sfile = os.path.join(dirname, file)
        if os.path.isfile(sfile):
            return sfile
        if not os.path.isabs(sfile):
            for rep in repositories:
                if os.path.isfile(os.path.join(rep, sfile)):
                    return sfile
    return None