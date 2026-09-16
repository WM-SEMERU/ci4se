def workspace_from_nothing(self, directory, mets_basename='mets.xml',
    clobber_mets=False):
    if directory is None:
        directory = tempfile.mkdtemp(prefix=TMP_PREFIX)
    if not exists(directory):
        makedirs(directory)
    mets_fpath = join(directory, mets_basename)
    if not clobber_mets and exists(mets_fpath):
        raise Exception("Not clobbering existing mets.xml in '%s'." % directory
            )
    mets = OcrdMets.empty_mets()
    with open(mets_fpath, 'wb') as fmets:
        log.info('Writing %s', mets_fpath)
        fmets.write(mets.to_xml(xmllint=True))
    return Workspace(self, directory, mets)