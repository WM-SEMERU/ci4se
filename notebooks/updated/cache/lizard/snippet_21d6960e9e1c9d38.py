def extract_module_name(absolute_path):
    base_name = osp.basename(osp.normpath(absolute_path))
    if base_name[0] in ('.', '_'):
        return None
    if osp.isdir(absolute_path):
        return base_name
    module_name, extension = osp.splitext(base_name)
    if extension == '.py':
        return module_name
    return None