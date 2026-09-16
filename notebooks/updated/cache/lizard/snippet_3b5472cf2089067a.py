def _check_path(self, src, path_type, dest=None, force=False):
    dest = dest or self.dest_path(src)
    if path_type == P_DIR:
        dest_dir = dest
    else:
        dest_dir = os.path.split(dest)[0]
    if not dest_dir:
        return dest
    if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
        raise ValueError("path '%s' exists and is not a directory" % dest_dir)
    elif not os.path.exists(dest_dir):
        src_dir = src if path_type == P_DIR else os.path.split(src)[0]
        self._make_leading_paths(src_dir)

    def is_special(mode):
        return any([stat.S_ISBLK(mode), stat.S_ISCHR(mode), stat.S_ISFIFO(
            mode), stat.S_ISSOCK(mode)])
    if force:
        return dest
    if os.path.exists(dest):
        st = os.lstat(dest)
        ve_msg = "path '%s' exists and is not a %s"
        if path_type == P_FILE and not stat.S_ISREG(st.st_mode):
            raise ValueError(ve_msg % (dest, 'regular file'))
        if path_type == P_LINK and not stat.S_ISLNK(st.st_mode):
            raise ValueError(ve_msg % (dest, 'symbolic link'))
        if path_type == P_NODE and not is_special(st.st_mode):
            raise ValueError(ve_msg % (dest, 'special file'))
        if path_type == P_DIR and not stat.S_ISDIR(st.st_mode):
            raise ValueError(ve_msg % (dest, 'directory'))
        return None
    return dest