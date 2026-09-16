def _install_toolplus(args):
    manifest_dir = os.path.join(_get_data_dir(), 'manifest')
    toolplus_manifest = os.path.join(manifest_dir, 'toolplus-packages.yaml')
    system_config = os.path.join(_get_data_dir(), 'galaxy', 'bcbio_system.yaml'
        )
    if not os.path.exists(system_config):
        docker_system_config = os.path.join(_get_data_dir(), 'config',
            'bcbio_system.yaml')
        if os.path.exists(docker_system_config):
            system_config = docker_system_config
    toolplus_dir = os.path.join(_get_data_dir(), 'toolplus')
    for tool in args.toolplus:
        if tool.name in set(['gatk', 'mutect']):
            print('Installing %s' % tool.name)
            _install_gatk_jar(tool.name, tool.fname, toolplus_manifest,
                system_config, toolplus_dir)
        else:
            raise ValueError('Unexpected toolplus argument: %s %s' % (tool.
                name, tool.fname))