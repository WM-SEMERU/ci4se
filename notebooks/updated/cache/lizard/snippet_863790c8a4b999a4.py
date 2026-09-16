def ManifestTools(**kargs):
    path_dirs = PathDirs(**kargs)
    manifest = join(path_dirs.meta_dir, 'plugin_manifest.cfg')
    template = Template(template=manifest)
    tools = template.sections()
    return tools[1]