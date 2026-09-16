def version_range(guid, version, before=None, app_versions=None):
    if app_versions is None:
        app_versions = validator.constants.APPROVED_APPLICATIONS
    app_key = None
    for app_guid, app_name in APPLICATIONS.items():
        if app_name == guid:
            guid = app_guid
            break
    for key in app_versions.keys():
        if app_versions[key]['guid'] == guid:
            app_key = key
            break
    if not app_key or version not in app_versions[app_key]['versions']:
        raise Exception(
            'Bad GUID or version provided for version range: %s' % version)
    all_versions = app_versions[app_key]['versions']
    version_pos = all_versions.index(version)
    before_pos = None
    if before is not None and before in all_versions:
        before_pos = all_versions.index(before)
    return all_versions[version_pos:before_pos]