def _get_manifest_dir(data=None, name=None):
    manifest_dir = None
    if data:
        bcbio_system = tz.get_in(['config', 'bcbio_system'], data, None)
        bcbio_system = bcbio_system if bcbio_system else data.get(
            'bcbio_system', None)
        if bcbio_system:
            sibling_dir = os.path.normpath(os.path.dirname(bcbio_system))
        else:
            sibling_dir = dd.get_galaxy_dir(data)
        if sibling_dir:
            manifest_dir = os.path.normpath(os.path.join(sibling_dir, os.
                pardir, 'manifest'))
    if not manifest_dir or not os.path.exists(manifest_dir):
        manifest_dir = os.path.join(config_utils.get_base_installdir(),
            'manifest')
        if not os.path.exists(manifest_dir) and name:
            manifest_dir = os.path.join(config_utils.get_base_installdir(
                name), 'manifest')
    return manifest_dir