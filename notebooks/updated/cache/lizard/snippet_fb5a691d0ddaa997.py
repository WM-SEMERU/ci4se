def get_module_names(package_path, pattern='lazy_*.py*'):
    package_contents = glob(os.path.join(package_path[0], pattern))
    relative_path_names = (os.path.split(name)[1] for name in package_contents)
    no_ext_names = (os.path.splitext(name)[0] for name in relative_path_names)
    return sorted(set(no_ext_names))