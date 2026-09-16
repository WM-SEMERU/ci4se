def make_dir_structure(base_dir):

    def maybe_makedir(*args):
        p = join(base_dir, *args)
        if exists(p) and not isdir(p):
            raise IOError("File '{}' exists but is not a directory ".format(p))
        if not exists(p):
            makedirs(p)
    maybe_makedir(DOWNLOAD_DIR)
    maybe_makedir(PACKAGE_DIR)
    maybe_makedir(OLD_DIR)