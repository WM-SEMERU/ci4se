def bookmark(snapshot, bookmark):
    if not __utils__['zfs.has_feature_flags']():
        return OrderedDict([('error', 'bookmarks are not supported')])
    target = []
    target.append(snapshot)
    target.append(bookmark)
    res = __salt__['cmd.run_all'](__utils__['zfs.zfs_command'](command=
        'bookmark', target=target), python_shell=False)
    return __utils__['zfs.parse_command_result'](res, 'bookmarked')