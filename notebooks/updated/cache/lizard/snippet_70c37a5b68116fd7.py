def _get_plugin_module_paths(self, plugin_dir):
    filepaths = [fp for fp in glob.glob('{}/**/*.py'.format(plugin_dir),
        recursive=True) if not fp.endswith('__init__.py')]
    rel_paths = [re.sub(plugin_dir.rstrip('/') + '/', '', fp) for fp in
        filepaths]
    module_paths = [rp.replace('/', '.').replace('.py', '') for rp in rel_paths
        ]
    return module_paths