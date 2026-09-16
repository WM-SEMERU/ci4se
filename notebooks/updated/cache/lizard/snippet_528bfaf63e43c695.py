def _get_versions(config=None):
    try:
        from bcbio.pipeline import version
        if hasattr(version, '__version__'):
            bcbio_version = '%s-%s' % (version.__version__, version.
                __git_revision__
                ) if version.__git_revision__ else version.__version__
        else:
            bcbio_version = ''
    except ImportError:
        bcbio_version = ''
    out = [{'program': 'bcbio-nextgen', 'version': bcbio_version}]
    manifest_dir = _get_manifest_dir(config)
    manifest_vs = _get_versions_manifest(manifest_dir) if manifest_dir else []
    if manifest_vs:
        out += manifest_vs
    else:
        assert config is not None, 'Need configuration to retrieve from non-manifest installs'
        brew_vs = _get_brew_versions()
        for p in _cl_progs:
            out.append({'program': p['cmd'], 'version': brew_vs[p['cmd']] if
                p['cmd'] in brew_vs else _get_cl_version(p, config)})
        for p in _alt_progs:
            out.append({'program': p['name'], 'version': brew_vs[p['name']] if
                p['name'] in brew_vs else p['version_fn'](config)})
    out.sort(key=lambda x: x['program'])
    return out