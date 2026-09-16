def build_software_cache(sw_dir=None):
    sw_dir = get_sw_dir(sw_dir)
    remove_software_cache(sw_dir)
    os.makedirs(sw_dir)
    reload_dependencies(force=True)
    for mod in deps:
        path = os.path.dirname(mod.__file__)
        name, ext = os.path.splitext(os.path.basename(mod.__file__))
        if name == '__init__':
            name = os.path.basename(path)
            shutil.copytree(path, os.path.join(sw_dir, name))
        else:
            shutil.copy2(os.path.join(path, name + '.py'), sw_dir)