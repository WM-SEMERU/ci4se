def CopyNoFail(src, root=None):
    if root is None:
        root = str(CFG['tmp_dir'])
    src_path = local.path(root) / src
    if src_path.exists():
        Copy(src_path, '.')
        return True
    return False