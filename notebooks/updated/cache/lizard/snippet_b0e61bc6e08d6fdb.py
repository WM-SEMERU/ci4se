def get_long_description():
    pkg_dir = get_package_dir()
    with open(os.path.join(pkg_dir, '.pypi_long_desc.rst')) as readme_file:
        long_description = readme_file.read()
    return long_description