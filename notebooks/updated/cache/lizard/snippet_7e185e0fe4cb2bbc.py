def remove(package_name):
    if package_name not in packages:
        raise HolodeckException('Unknown package name ' + package_name)
    for config, path in _iter_packages():
        if config['name'] == package_name:
            shutil.rmtree(path)