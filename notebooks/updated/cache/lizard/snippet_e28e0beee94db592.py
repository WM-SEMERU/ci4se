def get_version_string(check_name):
    version = VERSION.search(read_version_file(check_name))
    if version:
        return version.group(1)