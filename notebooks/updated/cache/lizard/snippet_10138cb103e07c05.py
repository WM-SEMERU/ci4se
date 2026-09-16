def render_cvmfs_sc(cvmfs_volume):
    name = CVMFS_REPOSITORIES[cvmfs_volume]
    rendered_template = dict(REANA_CVMFS_SC_TEMPLATE)
    rendered_template['metadata']['name'] = 'csi-cvmfs-{}'.format(name)
    rendered_template['parameters']['repository'] = cvmfs_volume
    return rendered_template