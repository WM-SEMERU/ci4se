def dictupdate(dest, upd, recursive_update=True, merge_lists=False):
    return salt.utils.dictupdate.update(dest, upd, recursive_update=
        recursive_update, merge_lists=merge_lists)