def __list_package_updates(package_name, version):
    updates = get_package_update_list(package_name, version)
    if updates['newer_releases'] or updates['pre_releases']:
        print('%s (%s)' % (package_name, version))
        __list_updates('Major releases', updates['major_updates'])
        __list_updates('Minor releases', updates['minor_updates'])
        __list_updates('Patch releases', updates['patch_updates'])
        __list_updates('Pre releases', updates['pre_release_updates'])
        __list_updates('Unknown releases', updates['non_semantic_versions'])
        print('___')