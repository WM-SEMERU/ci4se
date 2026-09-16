def file_present(container, name, path, profile, overwrite_existing=False):
    result = __salt__['libcloud_storage.download_object'](path, container,
        name, profile, overwrite_existing)
    return state_result(result, 'Downloaded object', name, {})