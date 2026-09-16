def make_srcdir_list(self, exclude_dirs):
    srcdir_list = []
    for topdir in self.topdirs:
        srcdir_list.append(topdir)
        srcdir_list += self.recursive_dir_list(topdir, exclude_dirs)
    return srcdir_list