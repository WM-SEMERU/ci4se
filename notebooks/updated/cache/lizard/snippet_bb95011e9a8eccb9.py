def get_namespace_url(module, version):
    module = module.strip('/')
    return '{module}/{name}'.format(module=get_namespace_module_url(module),
        name=get_namespace_file_name(module, version))