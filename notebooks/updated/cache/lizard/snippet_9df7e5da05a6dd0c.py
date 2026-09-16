def get_version_name(version_id):
    ver = registry.version_info.get(version_id)
    if ver:
        return ver.name
    return 'unknown'