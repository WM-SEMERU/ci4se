def file_attribs(location, mode=None, owner=None, group=None, use_sudo=
    False, recursive=True):
    return dir_attribs(location=location, mode=mode, owner=owner, group=
        group, recursive=recursive, use_sudo=False)