def UpdateManifestResourcesFromXML(dstpath, xmlstr, names=None, languages=None
    ):
    logger.info('Updating manifest in %s', dstpath)
    if dstpath.lower().endswith('.exe'):
        name = 1
    else:
        name = 2
    winresource.UpdateResources(dstpath, xmlstr, RT_MANIFEST, names or [
        name], languages or [0, '*'])