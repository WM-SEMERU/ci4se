def patch_init_py(base_dir, name, version):
    package_dir = os.path.join(base_dir, name)
    if not os.path.isdir(package_dir):
        os.makedirs(package_dir)
    init_py = os.path.join(package_dir, '__init__.py')
    log.info("patching %s to bake in version '%s'" % (init_py, version))
    with open(init_py, 'r+') as init_file:
        lines = init_file.readlines()
        try:
            begin = lines.index('# BEGIN VERSION CHECK\n')
            end = lines.index('# END VERSION CHECK\n')
        except ValueError:
            begin = end = len(lines)
        init_file.seek(0)
        init_file.writelines(lines[:begin] + lines[end + 1:])
        version_cmd = "__version__ = '{0}'\n".format(version)
        if not lines or lines[-1] != version_cmd:
            init_file.write('\n# Automatically added by katversion\n')
            init_file.write(version_cmd)
        init_file.truncate()